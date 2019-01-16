function login_fb(){
    window.location.href="https://waspfinance.auth.ap-southeast-1.amazoncognito.com/oauth2/authorize?response_type=code&client_id=7vtpik3iki7pfjnhgkuql06dej&redirect_uri=https://www.thewasp.co/login_facebook&identity_provider=Facebook&scope=aws.cognito.signin.user.admin+openid+profile";
    //window.location.href="http://127.0.0.1:5000/login_facebookcode=12345";
}
function login_google(){
    window.location.href="https://waspfinance.auth.ap-southeast-1.amazoncognito.com/oauth2/authorize?response_type=code&client_id=7vtpik3iki7pfjnhgkuql06dej&redirect_uri=https://www.thewasp.co/login_facebook&identity_provider=Google&scope=aws.cognito.signin.user.admin+openid+profile";
    //window.location.href="http://127.0.0.1:5000/login_facebookcode=12345";
}
