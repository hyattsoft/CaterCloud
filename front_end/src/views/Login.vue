<template>
    <el-container>
    <el-form :model="loginForm" :rules="fieldRules" ref="loginForm" label-position="left" label-width="0px" class="demo-ruleForm login-container">
    <h3 class="title">凯悦云餐饮--系统登陆</h3>
    <el-form-item prop="login_name">
      <el-input type="text" v-model="loginForm.login_name" auto-complete="off" placeholder="账号" clearable="true"></el-input>
    </el-form-item>
    <el-form-item prop="login_pass">
      <el-input type="password" v-model="loginForm.login_pass" auto-complete="off" placeholder="密码" clearable="true"></el-input>
    </el-form-item>
    <!-- <el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox> -->
    <el-form-item style="width:100%;">
      <el-button type="primary" style="width:48%;" @click.native.prevent="reset">重 置</el-button>
      <el-button type="primary" style="width:48%;" @click.native.prevent="login" :loading="logining">登 录</el-button>
    </el-form-item>
  </el-form>
</el-container>
</template>

<script>
    import Cookies from "js-cookie";
    export default {
    name: 'Login',
    data() {
      return {
        logining: false,
        loginForm: {
          login_name: 'admin',
          login_pass: '123456'
        },
        fieldRules: {
          login_name: [
            { required: true, message: '请输入账号', trigger: 'blur' },
          ],
          login_pass: [
            { required: true, message: '请输入密码', trigger: 'blur' },
          ]
        },
        checked: true
      };
    },
    methods: {
      login() {
        let userInfo = {login_name:this.loginForm.login_name, login_pass:this.loginForm.login_pass}
        this.$api.login(JSON.stringify(userInfo)).then((res) => {
            Cookies.set('token', res.data.token) // 放置token到Cookie
            sessionStorage.setItem('UserId', userInfo.login_name) // 保存用户到本地会话
            sessionStorage.setItem("logined", true)
            sessionStorage.setItem("Loginedname", userInfo.login_name)
            this.$router.push('/')  // 登录成功，跳转到主页
          }).catch(function(res) {
            alert(res);
          });
      },
      reset() {
        this.$refs.loginForm.resetFields();
      }
    }
    }
</script>

<style scoped lang="scss">
    .login-container {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #ffffff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
    .title {
      margin: 0px auto 40px auto;
      text-align: center;
      color: #505458;
    }
    .remember {
      margin: 0px 0px 35px 0px;
    }
  }
</style>