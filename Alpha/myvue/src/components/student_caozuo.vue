<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">

      <el-card style="width: 40%; margin: 10px">

        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <i class="el-icon-user"></i>
          <p>填写同组同学信息</p>

          <el-form-item label="sno" :label-width="formLabelWidth" prop="sno">
            <el-input style="width: 200px"
                      placeholder="请输入学号"
                      v-model="form.sno"
                      clearable>
            </el-input>
          </el-form-item>

          <el-form-item label="sname" :label-width="formLabelWidth" >
            <el-input style="width: 200px"
                      placeholder="请输入姓名"
                      v-model="form.sname"
                      clearable>
            </el-input>
          </el-form-item>

          <el-form-item label="sclass" :label-width="formLabelWidth" >
            <el-input style="width: 200px"
                      placeholder="请输入班级"
                      v-model="form.sclass"
                      clearable>
            </el-input>
          </el-form-item>

          <el-form-item label="sleader" :label-width="formLabelWidth" >
            <el-input style="width: 200px"
                      placeholder="请输入组长"
                      v-model="form.sleader"
                      clearable>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
        </el-form>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">添加</el-button>
        </div>

      </el-card>

      <el-card style="width: 40%; margin: 10px">

        <i class="el-icon-tickets"></i>
        <p>题库</p>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">查看全部</el-button>
        </div>

        <el-divider></el-divider>
        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="gotiku">！蹦到全部题库</el-button>
        </div>

        <el-divider></el-divider>

        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <el-form-item label="kno" :label-width="formLabelWidth" prop="kno">
            <el-input style="width: 200px"
                      placeholder="请输入题库号"
                      v-model="form.kno"
                      clearable>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
        </el-form>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">选择</el-button>
        </div>

        <p>注意！！！如何保证选择了就不能再选择了啊啊啊</p>

        <el-divider></el-divider>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">查看已选题库</el-button>
        </div>
        <p>显示了题库</p>

      </el-card>

      <el-card style="width: 40%; margin: 10px">

        <i class="el-icon-document-add"></i>
        <p>报告</p>

        <el-upload
          class="upload-demo"
          drag
          action="https://jsonplaceholder.typicode.com/posts/"
          multiple>
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        </el-upload>
      </el-card>

      <el-card style="width: 40%; margin: 10px">

        <i class="el-icon-lock"></i>
        <p>修改密码</p>

        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <el-form-item label="spass" :label-width="formLabelWidth" prop="spass">
            <el-input style="width: 200px"
                      placeholder="请输入新密码"
                      v-model="form.spass"
                      clearable>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
        </el-form>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">确认</el-button>
        </div>

      </el-card>

      <el-card style="width: 40%; margin: 10px">

        <i class="el-icon-trophy"></i>
        <p>成绩</p>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="save('form')">刷新</el-button>
        </div>

        <el-rate
          v-model="value"
          disabled
          show-score
          text-color="#ff9900"
          score-template="{value}">
        </el-rate>



      </el-card>


    </div>
  </div>
</template>

<script>
import request from "../util/request";

export default {
  name: "student_caozuo",
  data() {
    return {
      form:{
        sno: '',
        sname: '',
        sclass:'',
        sleader:'',
        kno:'',
        spass:'',
      },
      search: '',
      value: 3.7,//这里返回成绩
    };
  },

  methods: {

    gotiku(){
      this.$router.push({
        path:'../tiku'
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
