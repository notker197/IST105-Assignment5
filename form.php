<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Treasure Hunt</title>
</head>
<body>
    <h1>Welcome to the Interactive Treasure Hunt!</h1>
    <form action="process.php" method="POST">
        <label for="number">Number (e.g., birth year):</label>
        <input type="number" id="number" name="number" required><br><br>
        <label for="text">Text (e.g., name or secret word):</label>
        <input type="text" id="text" name="text" required><br><br>
        <input type="submit" value="Solve the Puzzle">
    </form>
</body>
</html>
