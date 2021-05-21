import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import globalVariable from './global_variable.js'
Vue.prototype.GLOBAL=globalVariable
import axios from 'axios'
Vue.use(ElementUI)

Vue.prototype.$axios = axios
Vue.config.productionTip = false
Vue.use(VueResource)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  data: function(){
		return {
			currentUser: '',//定义的全局变量
		}
	},
  components: { App },
  template: '<App/>'
})
