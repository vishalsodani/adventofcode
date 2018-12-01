use std::fs::File;
use std::io::{BufReader, BufRead};
use std::collections::HashSet;

fn main() {
	let f = File::open("input.txt").unwrap();
	let file = BufReader::new(f);
	let mut inputs = Vec::new();
	for line in file.lines() {
        let number: i32 = line.unwrap().parse().unwrap();
		inputs.push(number);
	}
	
	let mut scores = HashSet::new();
	let mut frequency = 0;
	let mut found_freqtwice = false;
	
	while found_freqtwice == false {
		for num in &inputs {
			frequency += num;
			if scores.contains(&frequency){
				found_freqtwice = true;
				println!("{}", frequency);
				break;
			}
			scores.insert(frequency);
		
		}
	
	
	}
}