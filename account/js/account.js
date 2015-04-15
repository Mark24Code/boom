current_edit_id = '';
function createNewCustomer(){
    $.ajax({
        url:'/account/api/customer/create/',
        type:'post',
        data:$('#create_form').serialize(),
        success:function(resp){
            if(resp.code == 200){
                $('#cancle_creating').click();
                location.reload();
                $('#create_form').find('input[type !="checkbox"]').val('');
                $('#create_form').find('input[type ="checkbox"]').attr('checked',false);
                $('#remark').val('');
            }
        },
        error:function(error){
            console.log('create_fail');
        }
    });
}

function edit_customer(id){
    current_edit_id = id;
    $.ajax({
        url:'/account/api/customer/edit/?customer_id='+id,
        type:'get',
        success:function(resp){
            console.log(resp.data.customer)
            var customer = resp.data.customer;
            
            for(var key in customer){
                $('#' + key + '_edit').val(customer[key])
            }

            $('#edit_customer_win').modal({keyboard: false});
        },
        error:function(error){
            console.log('edit_get_fail');
        }
    });
}

function saveEdit(){
    $.ajax({
        url:'/account/api/customer/edit/',
        type:'post',
        data:$('#edit_form').serialize(),
        success:function(resp){
            if(resp.code == 200){
                location.reload();
            }
        },
        error:function(error){
            console.log('edit_post_fail');
        }
    });
}

function del_product(){
    $.ajax({
        url:'/product/del?productId='+current_edit_id,
        type:'get',
        success:function(resp){
            if(resp.code == 200){
                $('#cancle_').click();
                location.reload();
            }
        },
        error:function(error){
            console.log('del_fail');
        }
    });
}

function createNewLog(){
    $.ajax({
        url:'/account/api/log/create/',
        type:'post',
        data:$('#create_form').serialize(),
        success:function(resp){
            if(resp.code == 200){
                $('#cancle_creating').click();
                location.reload();
                $('#create_form').find('input[type !="checkbox"][id != "id_edit"]').val('');
                $('#create_form').find('input[type ="checkbox"]').attr('checked',false);
                $('#remark').val('');
            }
        },
        error:function(error){
            console.log('create_fail');
        }
    });
}

function deleteLog(log_id){
    $.ajax({
        url:'/account/api/log/delete/?log_id='+log_id,
        type:'get',
        success:function(resp){
            if(resp.code == 200){
                $('#cancle_').click();
                $("#log_"+log_id).remove();
            }
        },
        error:function(error){
            console.log('del_fail');
        }
    });
}