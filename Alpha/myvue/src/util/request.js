import axios from 'axios'

const request = axios.create({ //创建一个request对象

  timeout: 5000
})

// 请求白名单，如果请求在白名单里面，将不会被拦截校验权限
// const whiteUrls = ["/user/login", '/user/register']

// // request 拦截器
// // 可以自请求发送前对请求做一些处理
// // 比如统一加token，对请求参数统一加密
// request.interceptors.request.use(config => {
//   config.headers['Content-Type'] = 'application/json;charset=utf-8';
//
//   return config
// }, error => {
//   return Promise.reject(error)
// });




export default request

