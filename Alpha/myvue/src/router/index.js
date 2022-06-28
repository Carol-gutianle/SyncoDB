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
      redirect:'/denglu', //这里是一开始的位置
      children:[

        {
          path: 'denglu',
          name: 'denglu',
          component: () => import("@/components/denglu")
        },

        {
          path: 'caozuo',
          name: 'caozuo',
          component: () => import("@/components/caozuo")
        },
    ]

    }

  ]
})
