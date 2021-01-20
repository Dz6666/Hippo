<template>
    <div class="show_center">
      <h1>展示中心页面 {{msg}}</h1>
      <a-button type="primary">Button</a-button>

      <div ref="main" id="main" style="width: 600px;height:400px;"></div>
    </div>
</template>

<script>
    export default {    // export 抛出对象，只有先抛出对象其他文件才可以引入组件
        name: "ShowCenter",
      // 组件对象.$echarts
      data(){
        return {
          msg:'hello',
        }
      },

      created() {

      },

      mounted() { //
        var myChart = this.$echarts.init(this.$refs.main);
        var option = {
          title: {
            text: 'ECharts 入门示例'
          },
          tooltip: {},
          legend: {
            data:['销量']
          },
          xAxis: {
            data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
          },
          yAxis: {},
          series: [{
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
          }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);

      }
    }
</script>

<style scoped>
  h1{
    color: olivedrab;
  }
</style>
