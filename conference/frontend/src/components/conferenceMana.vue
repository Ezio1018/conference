<template>
  <div class="home">

    <el-row display="margin-top:10px">
      <el-input v-model="input_conference_id" placeholder="请输入搜索会议室编号"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="showConferences()" style="float:left; margin: 2px;">搜索</el-button>
      <el-button type="primary" @click="addConferenceVisible = true" style="float:left; margin: 2px;">新增</el-button>
    </el-row>

    <el-row>
      <el-table :data="conferenceList" style="width: 100%" border>

        <el-table-column prop="conference_id" label="编号" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.conference_id }}</template>
        </el-table-column>

        <el-table-column prop="conference_capacity" label="容量" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.conference_capacity }}</template>
        </el-table-column>

        <el-table-column prop="conference_status" label="状态" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.conference_status ? '可用' : '维护中' }}</template>
        </el-table-column>

        <el-table-column prop="conference_authorization" label="权限" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.conference_authorization == 3 ? '高' : scope.row.fields.conference_authorization == 2 ? '中' : scope.row.fields.conference_authorization == 1 ? '低':'' }}</template>
        </el-table-column>

        <el-table-column label="操作" min-width="100">
          <template slot-scope="scope"><!--作用域插槽-->
            <el-button type="primary" icon="el-icon-edit" size="mini" @click="showEditDialog(scope.row.pk)"></el-button><!--scope.row表示当前这行的用户，用他的id去查询更新-->
            <el-button size="mini" type="danger" icon="el-icon-delete" @click="deleteConference(scope.row.pk)"></el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-row>

    <el-dialog
      title="添加记录"
      :visible.sync="addConferenceVisible"
      width="40%"
      @close="addConferenceVisible = false">
      <el-form ref="addFormRef" :rules="addFormRules" :model="addForm" label-width="100px">
        <el-form-item label="会议室编号" prop="conference_id">
          <el-input v-model="addForm.conference_id"></el-input>
        </el-form-item>
        <el-form-item label="会议室容量" prop="conference_capacity">
          <el-input v-model="addForm.conference_capacity"></el-input>
        </el-form-item>
        <el-form-item label="会议室状态" prop="conference_status">
          <el-select placeholder="请选择会议室状态" v-model="addForm.conference_status">
            <el-option label="可用" value="1"></el-option>
            <el-option label="维护中" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="会议室权限" prop="conference_authorization">
          <el-select placeholder="请选择会议室权限" v-model="addForm.conference_authorization">
            <el-option label="高" value="3"></el-option>
            <el-option label="中" value="2"></el-option>
            <el-option label="低" value="1"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <!--底部按钮区-->
      <span slot="footer" class="dialog-footer">
                <el-button @click="addConferenceVisible = false">取 消</el-button><!--点击取消隐藏对话框-->
                <el-button type="primary" @click="addConference">确 定</el-button><!--点击确定也会隐藏对话框-->
            </span>
    </el-dialog>

    <el-dialog
      title="修改会议室"
      :visible.sync="editConferenceVisible"
      width="50%"
      @close="editConferenceVisible = false"
    >
      <el-form ref="editFormRef" :rules="editFormRules" :model="editForm" label-width="100px">
        <el-form-item label="会议室编号" prop="conference_id">
          <el-input v-model="editForm.conference_id" ></el-input>
        </el-form-item>
        <el-form-item label="会议室容量" prop="conference_capacity">
          <el-input v-model="editForm.conference_capacity" ></el-input>
        </el-form-item>
        <el-form-item label="会议室状态" prop="conference_status">
          <el-select placeholder="请选择会议室状态" v-model="editForm.conference_status">
            <el-option label="可用" value="1"></el-option>
            <el-option label="维护中" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="会议室权限" prop="conference_authorization">
          <el-select placeholder="请选择会议室权限" v-model="editForm.conference_authorization">
            <el-option label="高" value="3"></el-option>
            <el-option label="中" value="2"></el-option>
            <el-option label="低" value="1"></el-option>
          </el-select>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer"><!--页脚-->
            <el-button @click="editConferenceVisible = false">取 消</el-button><!--隐藏对话框-->
            <el-button type="primary" @click="updateConference">确 定</el-button>
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
      var dulaConferenceid = (rule, value, callback) => {
        // 验证用户名是否存在.  一会再写
        this.$http.get('http://127.0.0.1:8000/api/select_conferenceByid?conference_id=' + this.addForm.conference_id)
          .then(response => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if(res['isExist'] === 1){
              callback(new Error('会议室已注册'))
            }else{
              callback()
            }
          })
      }
      return {
        addConferenceVisible: false,
        editConferenceVisible: false,
        input_conference_id: '',
        delete_conference_id: '',
        addForm: {},
        addFormRules: {
          conference_id: [
            {required: true, message: '请输入会议室编号', trigger: 'blur'},//鼠标移开不填的情况
            {min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur'},
            {validator: dulaConferenceid, trigger: 'blur'}
          ],
          conference_capacity: [
            {required: true, message: '请输入会议室容量', trigger: 'blur'},//鼠标移开不填的情况
            { validator: this.isNumber, trigger: 'blur' }
          ],
          conference_status: [
            {required: true, message: '请输入状态', trigger: 'blur'},//鼠标移开不填的情况
            // {validator: checkEmail, trigger: 'blur'}
          ],
          conference_authorization: [
            {required: true, message: '请输入权限', trigger: 'blur'},//鼠标移开不填的情况
            // {validator: checkMobile, trigger: 'blur'}//上面定义的正则表达式
          ]
        },//添加表单的验证规则对象
        editForm: {},
        editFormRules: {
          conference_capacity: [
            {required: true, message: '请输入会议室容量', trigger: 'blur'},//鼠标移开不填的情况
            { validator: this.isNumber, trigger: 'blur' }
          ],
          conference_status: [
            {required: true, message: '请输入状态', trigger: 'blur'},//鼠标移开不填的情况
            // {validator: checkEmail, trigger: 'blur'}
          ],
          conference_authorization: [
            {required: true, message: '请输入权限', trigger: 'blur'},//鼠标移开不填的情况
            // {validator: checkMobile, trigger: 'blur'}//上面定义的正则表达式
          ]
        },//添加表单的验证规则对象
        conferenceList: []
      }
    },
    mounted: function () {
      this.showConferences()
    },
    methods: {
      isNumber(rule, value, callback) {
        if (value === '') {
          return callback();
        }  //这是用来判断如果不是必须输入的，则直接跳出
        const r = /^\+?[1-9][0-9]*$/; // 正整数
        // 如果判断不符合正则，则不是正整数不能提交
        if (!r.test(value)) {
          return callback(new Error('数量必须为正整数'));
        } else {
          return callback();
        }
      },
      async addConference () {
        const {data: res} = await this.$http.post('http://127.0.0.1:8000/api/add_conference', this.addForm) // eslint-disable-line no-unused-vars
        this.addConferenceVisible = false
        if (res.error_num === 0) {
          this.$message.success('发布会议室成功')
          this.showConferences()
        }else{
          this.$message.error(res['msg'])
          this.showConferences()
        }
      },
      async updateConference () {
        const {data: res} = await this.$http.post('http://127.0.0.1:8000/api/update_conference', this.editForm) // eslint-disable-line no-unused-vars
        this.editConferenceVisible = false
        if (res.error_num === 0) {
          this.$message.success('更新会议室成功')
          this.showConferences()
        }else{
          this.$message.success(res['msg'])
          this.showConferences()
        }
      },
      showConferences () {
        this.$http.get('http://127.0.0.1:8000/api/show_conferences?conference_id=' + this.input_conference_id)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num === 0) {
              this.conferenceList = res['list']
            } else {
              this.$message.error('查询会议室失败')
              console.log(res['msg'])
            }
          })
      },
      async showEditDialog(updateid) {
        this.$http.get('http://127.0.0.1:8000/api/select_conference?id=' + updateid)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num === 0) {
              console.log(res['conference'])
              this.editForm = JSON.parse(res['conference'])
              console.log(typeof this.editForm.conference_authorization)
              this.editForm.conference_authorization = this.editForm.conference_authorization.toString()
              this.editForm.conference_status = this.editForm.conference_status.toString()
              console.log(typeof this.editForm.conference_authorization)
              console.log(this.editForm)
            } else {
              this.$message.error('显示失败')
              console.log(res['msg'])
            }
          })
        this.editConferenceVisible = true
      },
      deleteConference (delid) {
        console.log(delid)
        this.$http.get('http://127.0.0.1:8000/api/delete_conference?id=' + delid)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num === 0) {
              this.$message.success('删除会议室成功')
              this.showConferences()
            } else {
              this.$message.error('删除会议室失败，请重试')
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
