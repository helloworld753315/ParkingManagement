<template>
  <div class="container">
    <h1>駐車どう？</h1>
    <h2>空き情報</h2>
    <div class="info">
      <!--<p>{{data}}</p>-->
      <p>{{info}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Top',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App', 
      data:null
    }
  },
  computed: { // 関数として実装、参照時はプロパティとして機能
    info: function () {
      console.log("jikkou")
      if ((Number(this.data) / 10) < (1/3)){
        return "めっちゃ空いてる"
      }
      else if ((Number(this.data) / 10) > (1/2)){
        return "普通"
      }
      else if ((Number(this.data) / 10) > (3/4)){
        return "多すぎ"
      }
     //return this.data.unit
    }
  }, 
  created: function() {
    this.getPosts()
  },
  methods: {
        getPosts: function() {
      this.axios
        .get(
          "https://script.google.com/macros/s/AKfycbyKchRaXFsmLEBwLxiTb5Qs56Z6x2fw81pQOciek-S4nKvk3Gn3n4HiQ5RMObNjYC8YCQ/exec"
        )
        .then(response => {
          this.data = response.data[response.data.length-1].unit;
        })
    }
    
  },
  /*
  mounted () {
    fetch(
      'https://script.google.com/macros/s/AKfycbyKchRaXFsmLEBwLxiTb5Qs56Z6x2fw81pQOciek-S4nKvk3Gn3n4HiQ5RMObNjYC8YCQ/exec',
    )
      .then(res => res.json())
      .then(
      result => {
        this.data = result[result.length-1]
      },
      error => {

      },
    );
  }
  */
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}


.container h1{
  padding: 20px 60px;
  text-align: left;
}
.info{
  width: 400px;
  height: 100px;
  background: rgb(255, 171, 102);
  margin: 10px auto;

  border-radius: 10px;
}

.info p{
  padding: 40px;
}
</style>
