param(
    [int]$width = 20,
    [double]$speed = 0.1,
    [string]$char = '*',
    [int]$count = $null
)

# Build arg list
$argsList = @()
$argsList += "--width"; $argsList += $width.ToString()
$argsList += "--speed"; $argsList += $speed.ToString([System.Globalization.CultureInfo]::InvariantCulture)
$argsList += "--char"; $argsList += $char
if ($PSBoundParameters.ContainsKey('count')) { $argsList += "--count"; $argsList += $count.ToString() }

$scriptPath = Join-Path $PSScriptRoot "..\zigzag.py"
python $scriptPath @argsList
