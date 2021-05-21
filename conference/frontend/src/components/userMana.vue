<template>
  <div class="home">

    <el-row display="margin-top:10px">
      <el-input v-model="input_user_id" placeholder="请输入搜索用户编号"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="showUsers()" style="float:left; margin: 2px;">搜索</el-button>
      <el-button type="primary" @click="addUserVisible = true" style="float:left; margin: 2px;">新增</el-button>
    </el-row>

    <el-row>
      <el-table :data="userList" style="width: 100%" border>

        <el-table-column prop="user_id" label="编号" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.user_id }}</template>
        </el-table-column>

        <el-table-column prop="name" label="名字" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.name }}</template>
        </el-table-column>

        <el-table-column prop="gender" label="性别" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.gender }}</template>
        </el-table-column>

        <el-table-column prop="level" label="权限" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.level }}</template>
        </el-table-column>

        <el-table-column prop="department" label="部门" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.department }}</template>
        </el-table-column>

        <el-table-column prop="email" label="邮箱" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.email}}</template>
        </el-table-column>

        <el-table-column label="操作" min-width="100">
          <template slot-scope="scope"><!--作用域插槽-->
            <el-button type="primary" icon="el-icon-edit" size="mini" @click="showEditDialog(scope.row.pk)"></el-button>
            <el-button size="mini" type="danger" icon="el-icon-delete" @click="deleteUser(scope.row.pk)"></el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-row>

    <el-dialog
      title="添加记录"
      :visible.sync="addUserVisible"
      width="40%"
      @close="addUserVisible = false">
      <el-form ref="addFormRef" :rules="addFormRules" :model="addForm" label-width="100px">
        <el-form-item label="用户编号" prop="user_id">
          <el-input v-model="addForm.user_id"></el-input>
        </el-form-item>
        <el-form-item label="用户密码" prop="password">
          <el-input v-model="addForm.password"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="name">
          <el-input v-model="addForm.name"></el-input>
        </el-form-item>
        <el-form-item label="性别">
          <el-select v-model="addForm.gender" placeholder="请选择性别" style="display: block;">
            <el-option label="男" value="m"></el-option>
            <el-option label="女" value="w"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="用户权限" prop="level">
          <el-input v-model="addForm.level"></el-input>
        </el-form-item>
        <el-form-item label="部门" prop="department">
          <el-select v-model="addForm.department" placeholder="请选择部门" style="display: block;">
            <el-option label="技术部" value="技术部"></el-option>
            <el-option label="推广部" value="推广部"></el-option>
            <el-option label="客服部" value="客服部"></el-option>
            <el-option label="行政部" value="行政部"></el-option>
            <el-option label="财务部" value="财务部"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="addForm.email"></el-input>
        </el-form-item>
      </el-form>
      <!--底部按钮区-->
      <span slot="footer" class="dialog-footer">
                <el-button @click="addUserVisible = false">取 消</el-button><!--点击取消隐藏对话框-->
                <el-button type="primary" @click="addUser">确 定</el-button><!--点击确定也会隐藏对话框-->
            </span>
    </el-dialog>

    <el-dialog
      title="修改用户"
      :visible.sync="editUserVisible"
      width="50%"
      @close="editUserVisible = false"
    >
      <el-form ref="editFormRef" :rules="editFormRules" :model="editForm" label-width="100px">
        <el-form-item label="用户编号" prop="user_id">
          <el-input v-model="editForm.user_id"></el-input>
        </el-form-item>
        <el-form-item label="用户密码" prop="password">
          <el-input v-model="editForm.password"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="name">
          <el-input v-model="editForm.name"></el-input>
        </el-form-item>
        <el-form-item label="用户权限" prop="level">
          <el-input v-model="editForm.level"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="gender">
          <el-select v-model="editForm.gender" placeholder="请选择性别" style="display: block;">
            <el-option label="男" value="m"></el-option>
            <el-option label="女" value="w"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="部门" prop="department">
          <el-select v-model="editForm.department" placeholder="请选择部门" style="display: block;">
            <el-option label="技术部" value="技术部"></el-option>
            <el-option label="推广部" value="推广部"></el-option>
            <el-option label="客服部" value="客服部"></el-option>
            <el-option label="行政部" value="行政部"></el-option>
            <el-option label="财务部" value="财务部"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="editForm.email"></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer"><!--页脚-->
            <el-button @click="editUserVisible = false">取 消</el-button><!--隐藏对话框-->
            <el-button type="primary" @click="updateUser">确 定</el-button>
        <!--                修改的流程，点击修改按钮showEditDialog，查询到当前用户，对话框可见，输入要修改的属性，根据editFormRule
        s判断修改的合不合法，点击确定，触发editUserInfo，发起修改用户信息的数据请求，如果请求生成，关闭对话框，重新获取列表，提示更新成功-->
      </span>
    </el-dialog>

  </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      var checkEmail = (rule, value, cb) => {
        const regEmail = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/
        if (regEmail.test(value)) {
          return cb()
        }
        cb(new Error('请输入合法的邮箱'))
      }
      var dulaUsername = (rule, value, callback) => {
        // 验证用户名是否存在.  一会再写
        if (value.length < 3) {
          callback(new Error('你的用户名太短了！'))
        } else if (value.length > 18) {
          callback(new Error('你的用户名太长了！'))
        } else {
          this.$axios.post('/apis/api/register?select=1', {
            select_username: value
          })
            .then(response => {
              if (response.data.is_indb === 1) {
                callback(new Error('该用户名已经被注册'))
              } else {
                callback()
              }
            })
        }
      }
      return {
        addUserVisible: false,
        editUserVisible: false,
        input_user_id: '',
        delete_User_id: '',
        addForm: {},
        editForm: {},
        userList: [],
        addFormRules: {
          user_id: [
            //不知道为啥，下面这行有点问题，怎么输出都输出请输入用户名
            {required: true, message: '请输入账户', trigger: 'blur'},//鼠标移开不填的情况
            {min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur'},
            {validator: dulaUsername, trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'},//鼠标移开不填的情况
            {min: 6, max: 15, message: '长度在 6 到 15 个字符之间', trigger: 'blur'}
          ],
          email: [
            {required: true, message: '请输入邮箱', trigger: 'blur'},//鼠标移开不填的情况
            {validator: checkEmail, trigger: 'blur'}
          ],
        },
        editFormRules: {
          user_id: [
            //不知道为啥，下面这行有点问题，怎么输出都输出请输入用户名
            {required: true, message: '请输入账户', trigger: 'blur'},//鼠标移开不填的情况
            {min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur'},
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'},//鼠标移开不填的情况
            {min: 6, max: 15, message: '长度在 6 到 15 个字符之间', trigger: 'blur'}
          ],
          email: [
            {required: true, message: '请输入邮箱', trigger: 'blur'},//鼠标移开不填的情况
            {validator: checkEmail, trigger: 'blur'}
          ],
        },
      }

    },
    mounted: function () {
      this.showUsers()
    },
    methods: {
      async addUser () {
        const {data: res} = await this.$http.post('http://127.0.0.1:8000/api/add_user', this.addForm) // eslint-disable-line no-unused-vars
        this.addUserVisible = false
        if (res.error_num === 0) {
          this.$message.success('发布记录成功')
        }else{
          this.$message.error(res.msg)
        }
        this.showUsers()
      },
      async updateUser () {
        const {data: res} = await this.$http.post('http://127.0.0.1:8000/api/update_user', this.editForm) // eslint-disable-line no-unused-vars
        this.editUserVisible = false
        if (res.error_num === 0) {
          this.$message.success('发布记录成功')
        }else{
          this.$message.error(res.msg)
        }
        this.showUsers()
      },
      async showEditDialog(updateid) {
        this.$http.get('http://127.0.0.1:8000/api/select_user?id=' + updateid)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num === 0) {
              console.log(res['user'])
              this.editForm = JSON.parse(res['user'])
            } else {
              this.$message.error('查询失败')
              console.log(res['msg'])
            }
          })
        this.editUserVisible = true
      },
      showUsers () {
        this.$http.get('http://127.0.0.1:8000/api/show_users?user_id=' + this.input_user_id)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num === 0) {
              this.userList = res['list']
            } else {
              this.$message.error('查询用户失败')
              console.log(res['msg'])
            }
          })
      },
      deleteUser (delid) {
        console.log(delid)
        this.$http.get('http://127.0.0.1:8000/api/delete_user?id=' + delid)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num === 0) {
              this.$message.success('删除用户成功')
              this.showUsers()
            } else {
              this.$message.error('删除用户失败，请重试')
              console.log(res['msg'])
            }
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
