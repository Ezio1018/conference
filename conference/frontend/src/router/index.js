
import Vue from 'vue'
import Router from 'vue-router'
import home from '../components/home.vue'
// import HelloWorld from '@/components/HelloWorld'
// import Home from '@/components/Home'
import staff from '@/components/staff'
import face from '@/components/face'
import login from '@/components/login'
import firsthop from '@/components/firsthop'
import conferenceMana from '@/components/conferenceMana'
import conferenceBook from '@/components/conferenceBook'
import userMana from '@/components/userMana'
import formshow from '@/components/formshow'
import checkform from '@/components/checkform'
import profile from '@/components/profile/profile'
// import HelloWorld from '@/components/HelloWorld'
//import Home from '@/components/Home'
//import test from '@/components/test'

Vue.use(Router)
export default new Router({
  routes: [
    {path: '/', redirect: '/login'},
    {path: '/login', component: login},
    {path: '/face', component: face},
    {
      path: '/home',
      component: home,
      redirect: '/firsthop',
      children: [
        // eslint-disable-next-line no-undef
        {path: '/firsthop', component: firsthop},
        {path: '/userMana', component: userMana},
        {path: '/conferenceMana', component: conferenceMana},
        {path: '/conferenceBook', component: conferenceBook},
        {path: '/staff', component: staff},
        {path:'/profile', component:profile},
        {path: '/formshow', component: formshow},
        {path:'/checkform', component:checkform},
      ]
    }
  ]
}
)
