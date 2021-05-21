<template>
        <div >
            <ul>
                <li style="font-size:25px;font-family:KaiTi,serif;">昵称： {{this.Name}}</li>
                <li style="font-size:25px;font-family:KaiTi,serif;">用户名： {{this.Number}}</li>
                <li style="font-size:25px;font-family:KaiTi,serif;">角色： {{this.role_name == "user" ? '用户':this.role_name == "admin" ? '管理员' : '后勤职工'}}</li>
            </ul>
        </div>
</template>

<script>
    export default {
        name: "seeProfile",
        data(){
            return{
                Name: localStorage.user_name,
                Number: localStorage.user_id,
                role_name: localStorage.identity
            }
        },
        created(){
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            },
        }
    }
</script>

<style scoped>

</style>
