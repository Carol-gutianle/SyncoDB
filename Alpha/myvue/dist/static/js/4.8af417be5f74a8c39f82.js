webpackJsonp([4],{fX16:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=r("D/cR"),s={name:"add_deletelike",data:function(){return{form2:{username:""},search:"",rules:{username:[{required:!0,message:"请输入用户名",trigger:"blur"}],pass:[{required:!0,message:"请输入密码",trigger:"blur"},{min:6,max:6,message:"请输入6位数的密码",trigger:"blur"}]}}},methods:{handleDelete:function(e,t){var r=this;this.$refs[e].validate(function(e){e&&a.a.delete("/api/user/deleteUsers/"+t).then(function(e){console.log(e.data),0!==e.data?r.$message({type:"success",message:"删除成功"}):r.$message({type:"error",message:"数据库中没有"+t+"的信息"})})})}}},l={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("div",{staticStyle:{height:"40px"}}),e._v(" "),r("div",{staticStyle:{"text-align":"center",width:"100%","padding-left":"400px",margin:"auto"}},[r("div",[r("el-card",{staticStyle:{width:"30%",margin:"10px"}},[r("el-form",{ref:"form2",staticClass:"demo-ruleForm",attrs:{model:e.form2,"label-position":"left","label-width":"80px","status-icon":"",rules:e.rules}},[r("el-form-item",{attrs:{label:"username","label-width":e.formLabelWidth,prop:"username"}},[r("el-input",{staticStyle:{width:"200px"},attrs:{placeholder:"请输入内容",clearable:""},model:{value:e.form2.username,callback:function(t){e.$set(e.form2,"username",t)},expression:"form2.username"}})],1)],1),e._v(" "),r("div",{staticStyle:{"text-align":"center"}},[r("el-button",{attrs:{type:"primary",icon:"el-icon-delete"},on:{click:function(t){return e.handleDelete("form2",e.form2.username)}}},[e._v("删除")])],1)],1)],1)])])},staticRenderFns:[]};var n=r("VU/8")(s,l,!1,function(e){r("yTCk")},"data-v-716839c2",null);t.default=n.exports},yTCk:function(e,t){}});
//# sourceMappingURL=4.8af417be5f74a8c39f82.js.map