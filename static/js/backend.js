$(function(){


    $("#admin_login").validate({
        rules: {
            username: {
                required: true,
            },
            password: {
                required: true,
            },
        },
        
        messages: {
            username: "Username is required !",
            password: "Password is required !"
        },

        errorPlacement: function(error, element){
            if (element.attr("name") == "username"){
                $(".invalid-credential-hide").hide()
                error.appendTo("#username_error").css("color","#ff0000") 
            } else if (element.attr("name") == "password"){
                $(".invalid-credential-hide").hide()
                error.appendTo("#password_error").css("color","#ff0000")  
            }
        }
    });




   

    //filters
    $(".course_filter").on("change", function(){
        $("#all_course_search").val(null)
        let country = $("#selected_country").find("option:selected").val()
        let standard = $("#selected_class").find("option:selected").val()
        let language = $("#selected_language").find("option:selected").val()
        let type = $("#selected_type").find("option:selected").val()
        let csrf_token = Cookies.get("csrftoken")
        let url = `/control_panel/courses/`
        data = {
            "country": country,
            "class": standard,
            "language": language,
            "type": type
        }
        $.ajax({
            url: url,
            method: "POST",
            data: data,
            headers: {"X-CSRFToken": csrf_token},
            dataType: "json",
            success:function(data){
                $("#course_list_table_wrapper").empty();
                $("#course_list_table_wrapper").append(data['html_data']);
            }
        })
    });
    
})
