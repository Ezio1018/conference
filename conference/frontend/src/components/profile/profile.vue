<template>
    <div>
        <!--面包屑导航区域-->
        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/firsthop' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>个人信息</el-breadcrumb-item>
        </el-breadcrumb>

        <h2>个人信息</h2>
        
        <el-card>
            
            <el-tabs  :model="activeName" @tab-click="handleClick">
                <el-tab-pane  label="基本资料" name="基本资料">
                    <showProfile></showProfile>
                </el-tab-pane>
                <el-tab-pane label="密码修改" name="密码修改">
                    <editPassword></editPassword>
                </el-tab-pane>
            </el-tabs>
        </el-card>
    </div>
</template>

<script>
    import showProfile from "./showProfile";
    import editPassword from "./editPassword";
    export default {
        name: "profile",
        components:
            {showProfile,editPassword},
        data(){
            return{
                activeName: 'second',
            }
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            }
        }
    }
</script>

<style scoped>

</style>