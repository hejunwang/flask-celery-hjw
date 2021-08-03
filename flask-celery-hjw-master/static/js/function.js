

const  app1 = {
     delimiters:['[[',']]'],
    data(){
         return {
             message:'查询系统',
             count :2,
             sim :0
         }
    },
    methods:{
        add(){
            console.log('add click');
            this.count++;
        }
    }
}

Vue.createApp(app1).mount('#app')



const  appvue = {
    delimiters:['[[',']]'],
    data(){
        return {
            re:'',
            result: '异步任务进度',
            re1:'',
            result1: '异步任务进度1',
            sel:'',
            sel1:'异步任务执行'


        }
    },

    methods:
        {
            sendEmail(){
                axios.get('http://81.71.102.80:5000/req/add_task').
          then(response=>(this.result = response,this.re= response.data)).
                catch( function (error) {console.log(error)})
            },
            second(){
                axios.get('http://81.71.102.80:5000/req/second').
          then(response=>(this.result1 = response,this.re1= response.data)).
                catch( function (error) {console.log(error)})
            },

            select(){
                axios.get('http://81.71.102.80:5000/req/select').
          then(response=>(this.sel1 = response,this.sel= response.data)).
                catch( function (error) {console.log(error)})
            },


        }
}
Vue.createApp(appvue).mount('#one_')


// const  tt1 = {
//     delimiters:['[[',']]'],
//     data(){
//         return {
//             tt :10
//         }
//     },
//     mounted() {
//     setInterval(() => {
//       this.tt++
//     }, 1000)
//   }
// }
//
// Vue.createApp(tt1).mount('#app1')


const  we ={
    delimiters:['[[',']]'],
    data(){
        return {
            sim : 0
        }
    }

}
Vue.createApp(we).mount('#writeexcel')


