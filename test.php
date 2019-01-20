<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>クリックされたボタンに応じて処理を分岐する</title>
</head>
<body>
<?php
if (isset($_POST["sub1"])) {
	$kbn = htmlspecialchars($_POST["sub1"], ENT_QUOTES, "UTF-8");
	switch ($kbn) {
		case "A":
			exec("");
			//echo "登録処理";
			break; // A
		case "B":
			exec("")
			//echo "変更処理";
			break; // B
		case "C":
			exec("")
			//echo "削除処理";
			break; // C
		case "D":
			exec("")
			//echo "変更処理";
			break; // D
		case "E":
			exec("")
			//echo "変更処理";
			break; // E
		case "F":
			exec("")
			//echo "変更処理";
			break; // F
		case "G":
			exec("")
			//echo "変更処理";
			break; // G
		case "H":
			exec("")
			//echo "変更処理";
			break; // H
		case "I":
			exec("")
			//echo "変更処理";
			break; // I
		case "J":
			exec("")
			//echo "変更処理";
			break; // J
		case "K":
			exec("")
			//echo "変更処理";
			break; // K
		case "L":
			exec("")
			//echo "変更処理";
			break; // L
		default:
			//echo "エラー";
			exit;
	}
}
?>
<form method="POST" action="">
<input type="submit" value="A" name="sub1">
<input type="submit" value="B" name="sub1">
<input type="submit" value="C" name="sub1">
<input type="submit" value="D" name="sub1">
<input type="submit" value="E" name="sub1">
<input type="submit" value="F" name="sub1">
<input type="submit" value="G" name="sub1">
<input type="submit" value="H" name="sub1">
<input type="submit" value="I" name="sub1">
<input type="submit" value="J" name="sub1">
<input type="submit" value="K" name="sub1">
<input type="submit" value="L" name="sub1">
</form>
</body>
</html>

