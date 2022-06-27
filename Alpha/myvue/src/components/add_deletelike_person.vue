<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">
    <el-card style="width: 30%; margin: 10px">

    <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">


      <el-form-item label="username" :label-width="formLabelWidth" prop="username">
        <el-input style="width: 200px"
          placeholder="请输入内容"
          v-model="form.username"
          clearable>
        </el-input>
      </el-form-item>

      <el-form-item label="name" :label-width="formLabelWidth" >
        <el-input style="width: 200px"
          placeholder="请输入内容"
          v-model="form.name"
          clearable>
        </el-input>
      </el-form-item>

      <el-form-item label="age" :label-width="formLabelWidth"  prop="age">
        <el-input style="width: 200px"

          placeholder="请输入数字"
           v-model.number="form.age"
          clearable>
        </el-input>
      </el-form-item>
      <el-form-item label="teleno" :label-width="formLabelWidth">
        <el-input style="width: 200px"

          placeholder="请输入内容"
          v-model="form.teleno"
          maxlength="11"
          show-word-limit
          clearable>
        </el-input>
      </el-form-item>

      <div style="margin: 50px;"></div>
    </el-form>
      <div style="text-align: center">
        <el-button type="primary" icon="el-icon-edit" @click="save('form')">添加</el-button>
      </div>
    </el-card>



</div>
  </div>
</template>

<script>
import request from "../util/request";

export default {
  name: "add_deletelike_person",
  data() {
    var checkAge = (rule, value, callback) => {

      if (!value) {
        callback();
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字'));
        }
       else { callback();}
     }, 1000);

    };
    var namerule = (rule, value, callback) => {
        if (!value) {
          callback(new Error('请输入名称'));
        }
          else {callback();}
        };

    return {
      form:{
        username: '',
        name: '',
        teleno:'',
        age:''

      },


      search: '',
      rules: {
        username:[
          { required: true, message: '请输入用户名', trigger: 'blur' },

        ],
        namer:[
          { validator: namerule, trigger: 'blur'  },

        ],
        age: [
          { validator: checkAge, trigger: 'blur' }
        ]
      }
    };

  },

  methods: {
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
