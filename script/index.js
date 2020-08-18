function account_check() {
    let account = document.getElementById("login_account").value;
    let password = document.getElementById("login_password").value;
    if (account === '' || password === '') {
        alert("계정을 확인해주세요");
    } else
        console.log(account, password);
    };




