<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
</head>

<body>
<form action="form2.php" method="post">
<div id="apDiv1">
  <legend>Please fill  the form below: </legend>
  <p>
    <label>Fullname:
      <input type="text" name="Fullname" size="20" maxlength="40" />
    </label>
  </p>
  <p>
    <label>Surname:
      <input type="text" name="Surname" size="20" maxlength="40" />
    </label>
  </p>
  <p>
    <label>E-mail:
      <input type="text" name="Email" size="25" maxlength="60" />
    </label>
  </p>
  <p>
    <label>Telephone number:
      <input type="text" name="Telephone" size="20" maxlength="10" />
    </label>
  </p>
  <p>
    <label> Age </label>
    <input type="text" name="Age" size="5" maxlength="3" />
  </p>
</div>
<div id="apDiv2">
  <input type="submit" value="submit"/>
</div>
<div id="apDiv3"><a href="Homepage.html"><img src="../flask/Media/wonderful-homepage-icon-png-17.png" width="57" height="64" /></a></div>
<div id="apDiv4">Form</div>
<?php

error_reporting(E_ALL ^ E_DEPRECATED);
$con = mysql_connect("localhost","Pakis","PASSWORD");
$Fullname = $_REQUEST['Fullname'];
$Surname = $_REQUEST['Surname'];
$Email = $_REQUEST['Email'];
$Age = $_REQUEST['Age'];
$Telephone = $_REQUEST['Telephone'];

if (isset($_POST['submit'])){
$con = mysql_connect ["localhost"];
}
mysql_select_db("Project", $con);

$sql = "INSERT INTO Customs(Fullname, Surname, Email, Telephone, Age) VALUES ('$_POST[Fullname]', '$_POST[Surname]', '$_POST[Email]', '$_POST[Telephone]', '$_POST[Age]')";

mysql_query($sql, $con);

mysql_close($con);



?>

</body>
</html>