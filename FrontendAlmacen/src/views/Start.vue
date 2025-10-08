<script setup lang="ts">
import CreateUser from '../components/Forms/Users/CreateUser.vue'
import UpdateUser from '../components/Forms/Users/UpdateUser.vue'
import DeleteUser from '../components/Forms/Users/DeleteUser.vue'
import ArticleCreate from '../components/Forms/Articles/CreateArticle.vue';
import ArticleUpdate from '../components/Forms/Articles/UpdateArticle.vue';
import DeleteArticle from '../components/Forms/Articles/DeleteArticle.vue';
import CreateCompany from '../components/Forms/Companies/CreateCompany.vue';
import UpdateCompany from '../components/Forms/Companies/UpdateCompany.vue';
import DeleteCompany from '../components/Forms/Companies/DeleteCompany.vue';
import CreateCollaborator from '../components/Forms/Collaborators/CreateCollaborator.vue';
import UpdateCollaborator from '../components/Forms/Collaborators/UpdateCollaborator.vue';
import DeleteCollaborator from '../components/Forms/Collaborators/DeleteCollaborator.vue';
import CreateApplicationC from '../components/Forms/Applications/Collaborators/CreateCollaborators.vue';
import UpdateApplicationC from '../components/Forms/Applications/Collaborators/UpdateCollaborators.vue';
import DeleteApplicationC from '../components/Forms/Applications/Collaborators/DeleteCollaborators.vue';
import CreateApplicationCO from '../components/Forms/Applications/Consumables/CreateConsumable.vue';
import UpdateApplicationCO from '../components/Forms/Applications/Consumables/UpdateConsumable.vue';
import DeleteApplicationCO from '../components/Forms/Applications/Consumables/DeleteConsumable.vue';
import CreateApplicationT from '../components/Forms/Applications/Tools/CreateTools.vue';
import UpdateApplicationT from '../components/Forms/Applications/Tools/UpdateTools.vue';
import DeleteApplicationT from '../components/Forms/Applications/Tools/DeleteTools.vue';

</script>

<template>
    <label>Usuario</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateUser />
        </div>
        <div>
            <UpdateUser />
        </div>
        <div>
            <DeleteUser />
        </div>
        
    </div>
    <label>Empresa</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateCompany />
        </div>
        <div>
            <UpdateCompany />
        </div>
        <div>
            <DeleteCompany />
        </div>
        
    </div>
    <label>Colaborador</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateCollaborator />
        </div>
        <div>
            <UpdateCollaborator />
        </div>
        <div>
            <DeleteCollaborator />
        </div>
        
    </div>
    <label>Articulos</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <ArticleCreate />
        </div>
        <div>
            <ArticleUpdate />
        </div>
        <div>
            <DeleteArticle />
        </div>
    </div>

    <label>Colaboradores solicitud</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateApplicationC/>
        </div>
        <div>
            <UpdateApplicationC />
        </div>
        <div>
            <DeleteApplicationC /> 
        </div>
    </div>
    <label>Consumibles solicitud</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateApplicationCO/>
        </div>
        <div>
            <UpdateApplicationCO />
        </div>
        <div>
            <DeleteApplicationCO />
        </div>
    </div>
    <label>Herramientas solicitudes</label>
    <div class="grid grid-cols-3 grid-rows-1 gap-1">
        <div>
            <CreateApplicationT/>
        </div>
        <div>
            <UpdateApplicationT />
        </div>
        <div>
            <DeleteApplicationT />
        </div>
    </div>
</template>