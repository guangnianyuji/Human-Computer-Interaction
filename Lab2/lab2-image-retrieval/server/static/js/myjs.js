function imageshow(file) {
    var reader = new FileReader(); // 实例化一个FileReader对象，用于读取文件
    var source_img = document.getElementById('source_img'); // 获取要显示图片的标签

    //读取File对象的数据
    reader.onload = function (evt) {
        source_img.width = "180";
        source_img.height = "180";
        source_img.src = evt.target.result;
    }
    reader.readAsDataURL(file.files[0]);
}



var tags = new Array();
var phototag = new Array();
function imagesearch() {

    filename = $('#file').val;//value 属性包含了一个字符串，表示已选择文件的路径
    if (filename=="")
        return;
    console.log(filename);
    $('#load').show();
    $("form").submit(function (evt) {
        //$('#loader-icon').show();
        evt.preventDefault();
        //$('#loader-icon').show();
        var formData = new FormData($(this)[0]);
        $.ajax({
            url: 'imgUpload',
            type: 'POST',
            data: formData,
            //async: false,
            cache: false,
            contentType: false,
            enctype: 'multipart/form-data',
            processData: false,
            success: function (response) {
                $('#load').hide();

                //$('#clear').show();
                //console.log(response[1]);
                //document.getElementById("predictedResult").innerHTML= response;
                //先要设置tag => 动态添加button
                tags = response.tags
                console.log(tags)
                phototag = response.phototag
                for (var i = 0; i < tags.length; ++i) {
                    addrow(tags[i]);
                }
                //先展示图片
                document.getElementById("img0").src = response.image0[0];
                console.log(response.image0[0]);
                document.getElementById("img1").src = response.image1[0];
                document.getElementById("img2").src = response.image2[0];
                document.getElementById("img3").src = response.image3[0];
                document.getElementById("img4").src = response.image4[0];
                document.getElementById("img5").src = response.image5[0];
                document.getElementById("img6").src = response.image6[0];
                document.getElementById("img7").src = response.image7[0];
                document.getElementById("img8").src = response.image8[0];
               // console.log(response.image8[0]);
                $('#table').show();
                $('#tagtable').show();
                $('#clear').show();
                $('#favbtn').show();console.log("favbtn");
                //document.getElementById("img8").src = response.image8;

            }
        });
        return false;
    })
};

function addrow(name) {
    console.log("name is " + name)
    var c = document.getElementById('tagtable'); //获得表格的信息
   var row=c.rows[0];
    var cell = row.insertCell(0);//td元素
    cell.innerHTML+="<button id=\""+name+"\" type=\"button\"  class=\"btn btn-primary\" onclick=\"tagclick(this)\">" + name + "</button>"
}

function tagclick(name){
    console.log(phototag);
    console.log(name);
    id=name.id;
    console.log(id);
    if (name == "all"){//都展示
        for (var i=0;i<9;i++){
            $('#img'+i.toString()).show();
        }
        return;
    }
    for (var i=0;i<9;i++){
        var idstr='#img'+i.toString();
        console.log(idstr);
        console.log(phototag[i]);
        if(phototag[i].includes(id)){ //判断是否存在
            $(idstr).show();
            console.log("yes");
        }
        else{
            console.log("no");
            $(idstr).hide();
        }
    }
}

function reclear(){
   console.log("清理");
    $('#table').hide();
    $('#tagtable').hide();
    $('#clear').hide();
    $('#favbtn').hide();//收藏按钮藏起
    $('#fbtn').name='';//恢复收藏按钮的名字
    $('#fbtn').innerHTML="choose your like";//恢复收藏按钮的显示内容
    var c = document.getElementById('tagtable'); //获得标签表格的信息，删去标签表格
    var row=c.rows[0];
    var tagnumber = c.rows[0].cells.length;
    console.log(tagnumber);
    for(var i=tagnumber-2;i>=0;i--){
        row.deleteCell(i);
    }
     console.log(row);
}

function  choosefav(id){
    var btn=document.getElementById('fbtn');
    btn.innerHTML="Click here to like "+id;
    btn.name=id;
    console.log(btn.name);
}

var favstr= new Array();

function fav(name){
   if(name=="none"){
        return;
   }
   console.log(name);

   var photosrc = document.getElementById(name).src;
   var pl = photosrc.indexOf('im');
   var len=photosrc.length;
   photosrc=photosrc.substring(pl,len);//去掉前缀
   console.log(photosrc);

    if(!favstr.includes(photosrc)){
        favstr.push(photosrc);
        var favphotorow=document.getElementById('favphotorow');
        var ht="<div id=\" \""+"class=\"col-sm-2\"><img class=\"max\" src=\"dataset/"+photosrc+"\"></div>";
        console.log(ht);
        favphotorow.innerHTML+=ht;
        console.log(favphotorow.innerHTML);
    }
}