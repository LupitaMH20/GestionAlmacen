<script setup lang="ts">
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle,} from '@/components/ui/card'
import { User2 } from 'lucide-vue-next';
</script>

<template>
    <Card>
        <CardHeader>
            <CardTitle><User2/></CardTitle>
            <CardDescription>Card Description</CardDescription>
        </CardHeader>
        <CardContent>
            Card Content
        </CardContent>
        <CardFooter>
            Card Footer
        </CardFooter>
    </Card>
</template>