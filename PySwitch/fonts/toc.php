<?php
/**
 * Simple tool script: Delivers a JSON formatted TOC of all contained folders.
 */

function fillArrayWithFileNodes(DirectoryIterator $dir) {
    $data = array();
    foreach ($dir as $node) {
        //if (str_starts_with($node->getFilename(), ".")) continue;
        
        if ($node->isDir() && !$node->isDot()) {
            array_push($data, (object)array(
                "type" => $node->getType(),                
                "name" => $node->getFilename(),
                "children" => fillArrayWithFileNodes(new DirectoryIterator($node->getPathname()))
            ));

        } else if ($node->isFile()) {
            array_push($data, (object)array(
                "type" => $node->getType(),
                "name" => $node->getFilename()                
            ));            
        }
    }
    return $data;
}

$json = json_encode(
    (object)array(
        "type" => "dir",
        "name" => "",
        "path" => "",
        "children" => fillArrayWithFileNodes(new DirectoryIterator('.'))
    )
);

echo $json;
?>