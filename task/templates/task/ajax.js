
function ajax(conf) {

  var createAjax = function() {
    var xhr = null;
    try {
        //IE系列浏览器
        xhr = new ActiveXObject("microsoft.xmlhttp");
    } catch (e1) {
        try {
            //非IE浏览器
            xhr = new XMLHttpRequest();
        } catch (e2) {
            window.alert("您的浏览器不支持ajax，请更换！");
        }
    }
    return xhr;
  };

    // 初始化
    //type参数,可选
    var type = conf.type;
    //url参数，必填
    var url = conf.url;
    //data参数可选，只有在post请求时需要
    var data = conf.data;

    var contentType = conf.contentType;

    if(!(typeof data != 'undefined' && data instanceof FormData)){
      data = (function(obj){ // 转成post需要的字符串.
        var str = "";
        for(var prop in obj){
            str += prop + "=" + obj[prop] + "&"
        }
        return str.substring(0, str.length-1);
      })(data);
    }


    //datatype参数可选
    var dataType = conf.dataType;
    //回调函数可选
    var success = conf.success;
    var error=conf.error;
    if (type == null){
        //type参数可选，默认为get
        type = "get";
    }
    if (dataType == null){
        //dataType参数可选，默认为text
        dataType = "text";
    }
    // 创建ajax引擎对象
    var xhr = createAjax();
    // 打开
    xhr.open(type, url, conf.async == undefined ? true : conf.async);
    // 发送
    if (type == "GET" || type == "get") {
        xhr.send(null);
    } else if (type == "POST" || type == "post") {
      if(contentType){
        xhr.setRequestHeader("content-type", contentType);
      }else{
        if(!(contentType === false)){
          xhr.setRequestHeader("content-type",
                      "application/x-www-form-urlencoded");
        }

      }
        xhr.send(data);
    }
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if(dataType == "text"||dataType=="TEXT") {
                if (success != null){
                    //普通文本
                    success(xhr.responseText);
                }
            }else if(dataType=="xml"||dataType=="XML") {
                if (success != null){
                    //接收xml文档
                    success(xhr.responseXML);
                }
            }else if(dataType=="json"||dataType=="JSON") {
                if (success != null){
                    //将json字符串转换为js对象
                    success(eval("("+xhr.responseText+")"));
                }
            }
        }else if(xhr.readyState==4&&xhr.status!=200){
            error&&error.call(xhr, xhr.statusText, xhr.status);
        }
    };
};




  ajax({
      url: '/deep_receive.do?data={' + encodeURI(JSON.stringify(paramJson).replace('{', '').replace('}', '')) + '}',
      type: 'get',
      dataType: 'json',
      success: function(data) {
        if(data.errcode) {
          remindFn(data.msg);
          isClick = false;
        } else {
          remindFn('恭喜您获得奖励' + data.data.bonus/100);
          init();//获取奖励 修改状态
          isClick = false;
        }
      },
      error: function(){
        remindFn('无法领取奖励，请稍后尝试')
        isClick = false;
      }
    })
  }