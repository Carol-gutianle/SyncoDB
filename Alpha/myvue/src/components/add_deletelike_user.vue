<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">

    <div >
      <el-card style="width: 30%; margin: 10px">
      <el-form :model="form2"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form2">
        <el-form-item label="username" :label-width="formLabelWidth" prop="username">
          <el-input style="width: 200px"
            placeholder="请输入内容"
            v-model="form2.username"
            clearable>
          </el-input>
        </el-form-item>

      </el-form>
        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-delete" @click="handleDelete('form2',form2.username)">删除</el-button>
        </div>
      </el-card>

    </div>
    </div>

  </div>
</template>

<script>
import request from "../util/request";

export default {
  name: "add_deletelike",
  data() {
    return {

      form2:{username: ''},
      search: '',
      rules:{
        username:[
          { required: true, message: '请输入用户名', trigger: 'blur' },

        ],
        pass:[
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 6, message: '请输入6位数的密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods:{
    handleDelete(form2,username){
      this.$refs[form2].validate((valid) => {
        if (valid) {

          request.delete("/api/user/deleteUsers/"+username).then(res=>{
            console.log(res.data); //打印出来
            if ((res.data !== 0)){
              this.$message({
                type:"success",
                message:"删除成功"
              })
            }else{
              this.$message({
                type:"error",
                message:"数据库中没有"+username+"的信息"
              })
            }

          })

        }
      });
    }
  }
}
</script>

<style scoped>

</style>
