$().ready(function() {

  $.validator.addMethod("isPhone", function(value, element) {
          var length = value.length;
          var mobile = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1})|(17[0-9]{1}))+\d{8})$/;
          return this.optional(element) || (length == 11 && mobile.test(value));
         }, "请填写正确的手机号码");

  $.validator.addMethod("checkQQ",function(value,element,params){
          var checkQQ = /^[1-9][0-9]{4,19}$/;
          return this.optional(element)||(checkQQ.test(value));
         },"请输入正确的QQ号码");

// 在键盘按下并释放及提交后验证提交表单
  $("#changeuserinfoForm").validate({
    rules: {
      realname: {
        required: true,
      },
      email: {
        required: true,
        email: true
      },
      wechat: {
        required: true,
      },
      mobile: {
        required: true,
        isPhone:true
      },
      qq: {
        required: true,
        checkQQ:true
      }
    },
    messages: {
      realname: {
        required: "请输入真实姓名",
      },
      email: {
        required: "请输入邮箱",
        email: "请输入一个正确的邮箱"
      },
      wechat: {
        required: "请输入微信号码",
      },
      mobile: {
        required: "请输入手机号码",
      },
      qq: {
        required: "请输入QQ号码",
      }
     }
    })
});