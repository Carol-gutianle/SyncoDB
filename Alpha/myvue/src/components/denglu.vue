<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">
      <el-card style="width: 40%; margin: 10px">
        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <i class="el-icon-user-solid"></i>
          <p>数据库登录</p>

          <el-form-item label="用户名" :label-width="formLabelWidth" prop="username">
            <el-input style="width: 380px"
                      placeholder="请输入用户名"
                      v-model="form.username"
                      clearable>
            </el-input>
          </el-form-item>

          <!--之前input的style是 "width: 200px"，显示会歪，不知道应该怎么处理，经过调试改成380px可以解决-->

          <el-form-item label="密码" :label-width="formLabelWidth" prop="pwd">
            <el-input style="width: 380px"
                      placeholder="请输入密码"
                      v-model="form.pwd"
                      clearable
                      show-password>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
          <!--这个是底部空多少位置-->
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
import {L2Dwidget} from 'live2d-widget';

//检查用户名
var checktname = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入用户名'));
  }
  else {callback();}
};
//检查密码
var checktpass = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入密码'));
  }
  else {callback();}
};

export default {
  data() {
    return {
      form:{
        username: '',
        pwd:'',
      },
      search: '',

      rules: {
        username:[ { validator: checktname, trigger: 'blur'  }, ],
        pwd: [ { validator: checktpass, trigger: 'blur' } ]
      },

    };
  },

  methods:{
    save(form) {
      this.$refs[form].validate((valid) => {
        if (valid) {

          request.post("/api/checkConn/", this.form).then(res => {

            console.log(res.data); //打印出来
            if ((res.data.status == 200)) {
              this.$message({
                type: 'success',
                message: '连接成功！'
              })
              //跳转到操作界面
              this.gocaozuo();
            } else {
              this.$message({
                type: "error",
                message: "用户名/密码错误！"
              })
            }
          })
        }
      });
    },
  },

  created() {
      L2Dwidget.init({
        model: {
          jsonPath:"https://unpkg.com/live2d-widget-model-z16@1.0.5/assets/z16.model.json",
        }
      });
  }

}
</script>

<style scoped>
</style>
