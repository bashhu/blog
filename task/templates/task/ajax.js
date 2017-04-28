
function ajax(conf) {

  var createAjax = function() {
    var xhr = null;
    try {
        //IEϵ�������
        xhr = new ActiveXObject("microsoft.xmlhttp");
    } catch (e1) {
        try {
            //��IE�����
            xhr = new XMLHttpRequest();
        } catch (e2) {
            window.alert("�����������֧��ajax���������");
        }
    }
    return xhr;
  };

    // ��ʼ��
    //type����,��ѡ
    var type = conf.type;
    //url����������
    var url = conf.url;
    //data������ѡ��ֻ����post����ʱ��Ҫ
    var data = conf.data;

    var contentType = conf.contentType;

    if(!(typeof data != 'undefined' && data instanceof FormData)){
      data = (function(obj){ // ת��post��Ҫ���ַ���.
        var str = "";
        for(var prop in obj){
            str += prop + "=" + obj[prop] + "&"
        }
        return str.substring(0, str.length-1);
      })(data);
    }


    //datatype������ѡ
    var dataType = conf.dataType;
    //�ص�������ѡ
    var success = conf.success;
    var error=conf.error;
    if (type == null){
        //type������ѡ��Ĭ��Ϊget
        type = "get";
    }
    if (dataType == null){
        //dataType������ѡ��Ĭ��Ϊtext
        dataType = "text";
    }
    // ����ajax�������
    var xhr = createAjax();
    // ��
    xhr.open(type, url, conf.async == undefined ? true : conf.async);
    // ����
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
                    //��ͨ�ı�
                    success(xhr.responseText);
                }
            }else if(dataType=="xml"||dataType=="XML") {
                if (success != null){
                    //����xml�ĵ�
                    success(xhr.responseXML);
                }
            }else if(dataType=="json"||dataType=="JSON") {
                if (success != null){
                    //��json�ַ���ת��Ϊjs����
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
          remindFn('��ϲ����ý���' + data.data.bonus/100);
          init();//��ȡ���� �޸�״̬
          isClick = false;
        }
      },
      error: function(){
        remindFn('�޷���ȡ���������Ժ���')
        isClick = false;
      }
    })
  }