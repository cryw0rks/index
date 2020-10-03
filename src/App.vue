<template>
    <div class="cryw0rks-window">
        <div class="cry-title-bar">
            <div class="cry-title">{{ titleBar }}</div>
            <div class="cry-close" v-on:click="closeWindow">X</div>
        </div>
        <div class="cry-render">
            <transition :name="transitionName">
              <Sidebar v-if="sidebarShow"></Sidebar>
            </transition>
            <div class="cry-content">
                <transition :name="transitionName">
                  <router-view></router-view>
                </transition>
            </div>
        </div>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100;300;400;500;700;900&display=swap');

body {
    padding: 0;
    margin: 0;
    background: #AFAFAF;
    font-family: 'Noto Sans JP', sans-serif;
}

img {
    width: 20px;
}
</style>

<style>
.cryw0rks-window .cry-render {
  padding: 15px;
  height: calc(100% - 60px);
  overflow: hidden;
  display: table;
}

.cryw0rks-window .cry-render .cry-sidebar {
  width: 25%;
  display: table-cell;
  text-align: center;
  position: relative;
  vertical-align: top;
  padding-right: 15px;
  border-collapse: collapse;
}

.cryw0rks-window .cry-render .cry-sidebar img {
  width: 100%;
}

.cryw0rks-window .cry-render .cry-sidebar h3 {
  font-weight: 300;
  margin: 0;
  font-size: 15px;
}

.cryw0rks-window .cry-render .cry-sidebar p {
  font-size: 12px;
}

.cryw0rks-window .cry-render .cry-sidebar a {
  position: absolute;
  bottom: 5px;
  left: 0;
  width: calc(100% - 17px);
  background: #AFAFAF;
  text-decoration: none;
  color: #222222;
  padding: 10px 0;
  border: 1px solid #222222;
  font-weight: 500;
}

.cryw0rks-window .cry-render .cry-content .cry-box-title {
  margin: 0;
  font-weight: 400;
  font-size: 18px;
  padding: 0;
  margin-bottom: 5px;
}

.cryw0rks-window .cry-render .cry-content {
  display: table-cell;
  width: 75%;
  border-collapse: collapse;
  border: none;
  padding: 0;
  margin: 0;
}

.cryw0rks-window .cry-render .cry-content .cry-box-content {
  background: #ffffff;
  display: inline-block;
  border: 1px solid #222222; 
  padding: 5px;
  overflow-y: scroll;
  height: 269px;
  margin-top: 4px;
  width: calc(100% - 15px);
}

.cryw0rks-window .cry-render .cry-content .cry-box-content {
  font-size: 15px;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main {
  background: #ffffff;
  display: inline-block;
  border: 1px solid #222222; 
  padding: 5px;
  overflow-y: scroll;
  height: 269px;
  margin-top: 4px;
  width: calc(100% - 15px);
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list {
  display: inline-block;
  width: calc(50% - 2.5px);
  margin-bottom: 2px;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list:nth-child(odd) {
  margin-right: 5px;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside {
  height: 200px;
  padding: 10px 0px;
  position: absolute;
  width: 100%;
}


.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside .cry-work-content-name span {
  background: rgba(22, 22, 22, 0.8);
  padding: 5px 30px 5px 5px;
  display: inline-block;
  margin-bottom: 2px;
  color: #ffffff;
  font-weight: 400;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside .cry-work-content-name span b {
  font-weight: 900;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside .cry-work-content-website a,
.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside .cry-work-content-website a:visited,
.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside .cry-work-content-website a:link,
.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside .cry-work-content-website a:hover {
  background: rgba(22, 22, 22, 0.8);
  padding: 2px 6px;
  display: inline-block;
  font-size: 12px;
  text-decoration: none;
  color: #ffffff;
  font-weight: 400;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content-inside .cry-work-content-description p {
  position: absolute;
  bottom: 0;
  background: rgba(22, 22, 22, 0.8);
  font-size: 14px;
  width: 100%;
  color: #ffffff;
  text-align: center;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content {
  -webkit-transition: .5s;
  -o-transition: .5s;
  transition: .5s;
  border: 5px solid #222222;
  height: 220px;
  position: relative;
}

.cryw0rks-window .cry-render .cry-content .cry-work-main .cry-work-list .cry-work-content:hover {
  -webkit-transform: scale(0.9);
      -ms-transform: scale(0.9);
          transform: scale(0.9);
  -webkit-transition: .5s;
  -o-transition: .5s;
  transition: .5s;
}

.cryw0rks-window ul {
  margin-top: 5px;
}

.cryw0rks-window a, .cryw0rks-window a:link, .cryw0rks-window a:visited, .cryw0rks-window a:hover {
  color: #222222;
  font-weight: 900;
  text-decoration: none;
}

.fade-enter-active, .fade-leave-active {
  -webkit-transition: opacity .5s;
  -o-transition: opacity .5s;
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>

<style scoped>

.cryw0rks-window {
    width: 750px;
    height: 375px;
    background: #D3D3D3;
    top: 50%;
    left: 50%;
    position: absolute;
    -webkit-transform: translate(-50%,-50%);
        -ms-transform: translate(-50%,-50%);
            transform: translate(-50%,-50%);
    -webkit-box-shadow: 3px 3px 14px 3px rgba(0, 0, 0, 0.1);
            box-shadow: 3px 3px 14px 3px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.cryw0rks-window .cry-title-bar {
    background: #222222;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    height: 30px;
    position: relative;
}

.cryw0rks-window .cry-title-bar .cry-title {
    color: #FFFFFF;
    margin-top: 1px;
    margin-left: 10px;
}

.cryw0rks-window .cry-title-bar .cry-close {
    background: #FF5050;
    width: 30px;
    height: 100%;
    text-align: center;
    line-height: 1.7;
    right: 0;
    position: absolute;
    cursor: pointer;
}

@media only screen and (max-width: 750px) {
  .cryw0rks-window {
    position: relative;
    top: unset;
    left: unset;
    -webkit-transform: unset;
        -ms-transform: unset;
            transform: unset;
  }
}
</style>

<script>
import Sidebar from './components/Sidebar'

export default {
    data() {
        return {
            titleBar: null,
            sidebarShow: false,
            transitionName: 'fade'
        };
    },

    components: {
        Sidebar
    },
    
    methods: {
        closeWindow() {
            if (confirm("do you want to close window?")) {
                alert('lmao, close button is not working :P');
                //close();
            //} else {
                //open('/');
            }
        },

        componentRender() {
            this.titleBar = this.$route.name;
            document.title = this.titleBar;
            if (this.$route.name == "cryw0rks.exe") {
                setTimeout(function() { this.sidebarShow = false; }.bind(this), 0);
            } else {
                setTimeout(function() { this.sidebarShow = true; }.bind(this), 500);
            }
        }
    },

    mounted() {
        this.componentRender();
    },

    updated() {
        this.componentRender();
    }
};
</script>