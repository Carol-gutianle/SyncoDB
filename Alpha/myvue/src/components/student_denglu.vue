<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">
      <el-card style="width: 40%; margin: 10px">
        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <i class="el-icon-user-solid"></i>
          <p>学生登录</p>

          <el-form-item label="sname" :label-width="formLabelWidth" >
            <el-input style="width: 200px"
                      placeholder="请输入姓名"
                      v-model="form.sname"
                      clearable>
            </el-input>
          </el-form-item>

          <el-form-item label="spass" :label-width="formLabelWidth" >
            <el-input style="width: 200px"
                      placeholder="请输入密码"
                      v-model="form.spass"
                      clearable>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
        </el-form>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">登录</el-button>
        </div>

        <el-divider></el-divider>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="gocaozuo">跳转到学生操作</el-button>
        </div>

      </el-card>
    </div>
  </div>
</template>

<script>
import request from "../util/request";

export default {
  name: "student_denglu",
  data() {
    //检查姓名
    var checksname = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入名字'));
      }
      else {callback();}
    };
    //检查密码
    var checkspass = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入密码'));
      }
      else {callback();}
    };

    return {
      form:{
        sname: '',
        spass:'',
      },
      search: '',

      rules: {
        sname:[ { validator: checksname, trigger: 'blur'  }, ],
        spass:[ { validator: checkspass, trigger: 'blur'  } ]
      }
    };
  },

  methods: {
    gocaozuo(){
      this.$router.push({
        path:'../student_caozuo'
      })
    },



    save(form) {
      this.$refs[form].validate((valid) => {
        if (valid) {

          request.post("/api/person/addPerson", this.form).then(res => {

            console.log(res.data); //打印出来
            if ((res.data !== 0)) {
              if ((res.data === 1)){
                this.$message({
                  type: "success",
                  message: "成功添加"+this.form.name
                })
              }else{
                this.$confirm("用户名"+this.form.username+"已存在，需要修改信息吗？", '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
                }).then(() => {
                  request.put("/api/person/updatePerson",this.form).then(res=> {
                    console.log(res) //打印出来
                    if (res.code !== '0') {
                      this.$message({
                        type: "success",
                        message: "修改成功"
                      })

                    }
                  });

                }).catch(() => {
                  this.$message({
                    type: 'info',
                    message: '已取消修改'
                  });
                });
              }

            } else {
              this.$message({
                type: "error",
                message: "名称"+this.form.name+"重复,请重新填写"
              })
            }
          })
        }
      });
    },
  }

}
</script>





<style scoped>

</style>
