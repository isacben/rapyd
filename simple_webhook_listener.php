<?php
/**
 * simple_webhook_listener.php
 *
 * Get notifications from Rapyd webhooks and logs them to a file.
 *
 * Deploy this file to a PHP Webserver. Then configure the listener
 * in the Rapyd Client Portal with the listener URL. For example:
 * 
 * https://exaple.com/simple_webhook_listener.php
 *
 * Finally open the output file to see the results. For example:
 * 
 * https://exaple.com/output.txt
 *
 * @author     Isaac Benitez
 * @version    1.0.0
 * @datetime   07/02/2021
 * 
 */

$data = file_get_contents("php://input");
$parsed_data = json_decode($data, true); // optional: if parsed data needed

// save the raw data into a file
$o_file = fopen("output.txt", "a") or die("Unable to open file!");

$info = "Notification received...\n";
fwrite($o_file, $info);

// append the data as it is received into the file
fwrite($ofile, $data);

fclose($ofile);

?>
