import Intro from './../apps/main/main.vue'
//const Intro= { template: '<div>intro</div>' }

const Article = {
    template: `
    <div class="article">
        <h2>Article</h2>
        <router-view></router-view>
        </div>
        `
    }
const ArticleList = { template: '<div>article list</div>' }
const ArticleWrite = { template: '<div>article write</div>' }
const Mypage = { template: '<div>mypage</div>' }

const routes = [
    { path: '/', component: Intro },
    { path: '/mypage', component: Mypage },
    { path: '/article', component: Article,
        children: [
            {
                path: 'write',
                component: ArticleWrite
            },
            {
                path: '',
                component: ArticleList
            }
        ]
    }
]

const router = new VueRouter({
    routes,
    mode: 'history'
})

const app = new Vue({
    router,
    el: '#app',
    delimiters: ['${', '}'], //django와 연동하기 위해 interpolation delimiters 변경
    data: {
        message: 'Article Box입니다!'
    }
}).$mount('#app')