<template>
  <div class="cry-home">
      <img alt="Vue logo" src="../assets/logo.png">
      <h3>クライワークス</h3>
      <p>select one program you want to run, powered by <a href="https://ba-ka.org/">ba-ka</a></p>
      <p>designed by <a href="https://ah0.ba-ka.org/user/4km">4k_m4</a>, code by <a href="https://ah0.ba-ka.org/user/datoyacx">datoyacx</a></p>
      <ul>
        <li><router-link to="/service">service</router-link></li>
        <li><router-link to="/portfolio">portfolio</router-link></li>
        <li><router-link to="/project">project</router-link></li>
        <li><router-link to="/contact">contact</router-link></li>
      </ul>
  </div>
</template>

<style>
.cryw0rks-window p {
  font-weight: 300;  
  font-size: 12px;
}

.cryw0rks-window .cry-home {
  text-align: center;
  padding: 20px;
  margin-bottom: 30px;
}

.cryw0rks-window .cry-home img {
  width: 30%;
}

.cryw0rks-window .cry-home h3 {
  margin: 0;
  font-weight: 300;
}

.cryw0rks-window .cry-home ul {
  list-style: none;
  padding: 0;
  margin: 0;
  margin-top: 30px;
}

.cryw0rks-window .cry-home ul li {
  display: inline-block;
  margin: 0 10px;
}

.cryw0rks-window .cry-home ul li a,
.cryw0rks-window .cry-home ul li a:visited,
.cryw0rks-window .cry-home ul li a:link,
.cryw0rks-window .cry-home ul li a:hover {
  text-decoration: none;
  color: #222222;
  background: #ffffff;
  padding: 10px 25px;
  border: 1px solid #222222;
  font-weight: 500;
  display: block;
}

.cryw0rks-window .cry-home ul li:nth-child(1) a,
.cryw0rks-window .cry-home ul li:nth-child(1) a:visited,
.cryw0rks-window .cry-home ul li:nth-child(1) a:link,
.cryw0rks-window .cry-home ul li:nth-child(1) a:hover {
  background: #FFCDCD;
}

.cryw0rks-window .cry-home ul li:nth-child(2) a,
.cryw0rks-window .cry-home ul li:nth-child(2) a:visited,
.cryw0rks-window .cry-home ul li:nth-child(2) a:link,
.cryw0rks-window .cry-home ul li:nth-child(2) a:hover {
  background: #D9FFCD;
}

.cryw0rks-window .cry-home ul li:nth-child(3) a,
.cryw0rks-window .cry-home ul li:nth-child(3) a:visited,
.cryw0rks-window .cry-home ul li:nth-child(3) a:link,
.cryw0rks-window .cry-home ul li:nth-child(3) a:hover {
  background: #FFCDF3;
}

.cryw0rks-window .cry-home ul li:nth-child(4) a,
.cryw0rks-window .cry-home ul li:nth-child(4) a:visited,
.cryw0rks-window .cry-home ul li:nth-child(4) a:link,
.cryw0rks-window .cry-home ul li:nth-child(4) a:hover {
  background: #CDE8FF;
}
</style>

<script>
export default {
    mounted () {
        var audio = new Audio(require('../assets/intro.mp3'));
        audio.play();
    } 
};
</script>