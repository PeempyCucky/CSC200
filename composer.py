import json
import os
import php
import composer
<?php

require_once 'vendor/autoload.php'; // skip this if using a framework / autoloading elsewhere

use JasonRoman\NbaApi\Client\Client;
use JasonRoman\NbaApi\Request\Data\Prod\Game\BoxscoreRequest;

$client = new Client();

$request = BoxscoreRequest::fromArray([
    'gameDate' => new \DateTime('2017-02-01'),
    'gameId'   => '0021600732',
]);

$response = $client->request($request);
