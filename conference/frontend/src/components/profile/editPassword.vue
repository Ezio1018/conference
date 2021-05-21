<template>
    <div>
        <div class="edit_box">
            <el-form :model="editForm" style="width: 100px">
                <el-form-item label="新密码" prop="password1" style="font-size:25px" placeholder="请输入用户名" label-width="100px"><!--prop="userNumber"是指定用户规则-->
                    <el-input v-model="editForm.password1" type="password" style="width:350px;font-size: 20px;"></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="password2" style="font-size:25px" placeholder="请输入用户名" label-width="100px"><!--prop="userNumber"是指定用户规则-->
                    <el-input v-model="editForm.password2" type="password" style="width:350px;font-size: 20px;"></el-input>
                </el-form-item>
                <el-form-item class="btns">
                    <el-button type="primary" @click="editPassword">确定</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "editPassword",
        data(){
            return{
                editForm:{
                    user_id : localStorage.user_id,
                    password1:'',
                    psaaword2:'',
                },
            }
        },
        methods:{
            async editPassword(){//修改密码是所有角色通用的
                if(this.editForm.password1===this.editForm.password2) {
                  const {data: res} = await this.$http.post('http://127.0.0.1:8000/api/editPassword', this.editForm) // eslint-disable-line no-unused-vars
                  if (res.error_num === 0) {
                    this.$message.success('更新密码成功')
                    this.showConferences()
                  } else {
                    this.$message.success(res['msg'])
                    this.showConferences()
                  }
                }
            }
        }
    }
</script>

<style>
    .edit_box{
        width:500px;
        height:330px;
    }
    .btns{
        display: flex;/*水平居于有对齐*/
        justify-content: flex-end;
        position:relative;
        left:350px
    }

</style>
