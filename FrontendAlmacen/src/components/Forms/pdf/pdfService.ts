import apiClient from '@/lib/axios';

export const PdfService = {
    async downloadEquipmentCheckout(requestId: number | string) {
        try {
            const config = {
                responseType: 'blob' as const
            };
            const url = `request/${requestId}/checkout-pdf/`
            const response = await apiClient.get(url, config)

            // Crear URL del blob
            const blob = new Blob([response.data], { type: 'application/pdf' });
            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = `Resguardo_Equipo_${requestId}.pdf`;
            link.click();
            window.URL.revokeObjectURL(link.href);
        } catch (error) {
            console.error('Error descargando PDF:', error);
            throw error;
        }
    },

    async downloadQuotePdf(requestId: number | string) {
        try {
            const config = {
                responseType: 'blob' as const
            };
            const url = `request/${requestId}/quote-pdf/`
            const response = await apiClient.get(url, config)

            // Crear URL del blob
            const blob = new Blob([response.data], { type: 'application/pdf' });
            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = `Cotizacion_${requestId}.pdf`;
            link.click();
            window.URL.revokeObjectURL(link.href);
        } catch (error) {
            console.error('Error descargando PDF de cotización:', error);
            throw error;
        }
    },

    async downloadBulkQuotePdf(requestIds: (number | string)[]) {
        try {
            const config = {
                responseType: 'blob' as const
            };
            const url = `request/bulk-quote-pdf/`
            const response = await apiClient.post(url, { request_ids: requestIds }, config)

            // Crear URL del blob
            const blob = new Blob([response.data], { type: 'application/pdf' });
            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = `Reporte_Solicitudes.pdf`;
            link.click();
            window.URL.revokeObjectURL(link.href);
        } catch (error) {
            console.error('Error descargando PDF masivo:', error);
            throw error;
        }
    }
}
