import Vue from 'vue'
import VueRouter from 'vue-router'
import layout from '../layout/layout.vue'
Vue.use(VueRouter)
export default new VueRouter({
  routes:[
    {
      path: '/',
      name:'layout',
      component: layout,
      redirect:'/add_deletelike_person',
      children:[
      {
        path: 'add_deletelike_person',
        name: 'add_deletelike_person',
        component: () => import("@/components/add_deletelike_person")
      },


        {
          path: 'student_denglu',
          name: 'student_denglu',
          component: () => import("@/components/student_denglu")
        },

        {
          path: 'student_caozuo',
          name: 'student_caozuo',
          component: () => import("@/components/student_caozuo")
        },

        {
          path: 'teacher_denglu',
          name: 'teacher_denglu',
          component: () => import("@/components/teacher_denglu")
        },

        {
          path: 'teacher_caozuo',
          name: 'teacher_caozuo',
          component: () => import("@/components/teacher_caozuo")
        },

        {
          path: 'teacher_caozuo2',
          name: 'teacher_caozuo2',
          component: () => import("@/components/teacher_caozuo2")
        },

        {
          path: 'tiku',
          name: 'tiku',
          component: () => import("@/components/tiku")
        },

        {
          path: 'tourist_denglu',
          name: 'tourist_denglu',
          component: () => import("@/components/tourist_denglu")
        },

      {
        path: 'add_deletelike_user',
        name: 'add_deletelike_user',
        component: () => import("@/components/add_deletelike_user")
      },
      {
        path: 'home',
        name: 'home',
        component: () => import("@/components/home")
      },
      {
        path: 'userhome',
        name: 'userhome',
        component: () => import("@/components/userhome")
      }
    ]

    }

  ]
})
