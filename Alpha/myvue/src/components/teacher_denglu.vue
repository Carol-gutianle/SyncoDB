<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">
      <el-card style="width: 40%; margin: 10px">
        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <i class="el-icon-user-solid"></i>
          <p>数据库连接</p>

          <el-form-item label="账号" label-width="formLabelWidth" prop="tno">
            <el-input style="width: 200px"
                      placeholder="请输入账号"
                      v-model="form.tno"
                      clearable>
            </el-input>
          </el-form-item>

          <el-form-item label="密码" label-width="formLabelWidth" prop="tpwd">
            <el-input style="width: 200px"
                      placeholder="请输入密码"
                      v-model="form.tpwd"
                      clearable>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
        </el-form>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">登录</el-button>
        </div>
      </el-card>
    </div>
  </div>
</template>




<script>
import request from "../util/request";

export default {
  name: "teacher_denglu",
  data() {
    //检查账号
    var checktno = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('请输入工资号'));
      }
      else {callback();}
    };
    //检查密码
    var checktpwd = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入密码'));
      }
      else {callback();}
    };

    return {
      form:{
        tno: '',
        tpwd:'',
      },
      rules: {
        tno:[ { validator: checktno, trigger: 'blur'  }, ],
        tpwd: [ { validator: checktpwd, trigger: 'blur' } ]
      }
    };
  },

  methods:{
    gocaozuo(){
      this.$router.push({
        path:'../teacher_caozuo',
        query: {
          tno: this.form.tno
        }
      })
    },
    save(form) {
      this.$refs[form].validate((valid) => {
        if (valid) {
          var qs = require('querystring')
          console.log(this.form)
          request.post("/teaLogin", qs.stringify(this.form)).then(res => {
            if(res.data.code===200) {
              this.gocaozuo()
            } else {
              this.$message({
                type: "error",
                message: "账号或密码错误！"
              })
            }
          })
        }
        else {
          console.log('error')
        }
      });

    },
  }}
</script>

<style scoped>

</style>
