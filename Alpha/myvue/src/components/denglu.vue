<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">
      <el-card style="width: 40%; margin: 10px">
        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <i class="el-icon-user-solid"></i>
          <p>数据库登录</p>

          <el-form-item label="用户名" :label-width="formLabelWidth" >
            <el-input style="width: 200px"
                      placeholder="请输入姓名"
                      v-model="form.username"
                      clearable>
            </el-input>
          </el-form-item>

          <el-form-item label="密码" :label-width="formLabelWidth" >
            <el-input style="width: 200px"
                      placeholder="请输入密码"
                      v-model="form.pwd"
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
import {L2Dwidget} from 'live2d-widget';

export default {
  name: "teacher_denglu",
  data() {
    //检查姓名
    var checktname = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入名字'));
      }
      else {callback();}
    };
    //检查姓名
    var checktpass = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入密码'));
      }
      else {callback();}
    };

    return {
      form:{
        username: '',
        pwd:'',
      },
      search: '',

      rules: {
        username:[ { validator: checktname, trigger: 'blur'  }, ],
        pwd: [ { validator: checktpass, trigger: 'blur' } ]
      }
    };
  },

  methods:{

    gocaozuo(){
      this.$router.push({
        path:'../caozuo'
      })
    },

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
