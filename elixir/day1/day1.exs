IO.puts File.stream!("input.txt")
|> Enum.to_list
|> Enum.map(fn (x) -> String.trim(x) end)
|> Enum.map(fn (x) -> String.to_integer x end)
|> Enum.sum





