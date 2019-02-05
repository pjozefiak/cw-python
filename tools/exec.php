<?php

require_once( dirname(__FILE__) . '/../../../../../wp-load.php' );

global $wpdb;

function phpTest() {
        exec('php -i', $out);
        $match = array_values(preg_grep("/.SERVER\['PATH'\]/i", $out));
        return substr($match[0], 20);
    }

echo phpTest();
echo "<br />" . $_SERVER['PATH'];
