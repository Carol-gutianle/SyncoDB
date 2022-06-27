//该文件专门用于创建整个应用的路由
import VueRouter from 'vue-router'
//引入组件
import sc from '../components/student_caozuo'
import tc from '../components/teacher_caozuo'

//创建并暴露一个路由器
export default new VueRouter({
  routes:[
    {
      path:'../components/student_caozuo',
      component:sc
    },
    {
      path:'../components/teacher_caozuo',
      component:tc
    }
    ]
})
