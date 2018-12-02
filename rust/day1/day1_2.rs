use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let f = File::open("../../inputs/day1/input.txt").unwrap();
	let mut frequency = 0;
	let file = BufReader::new(f);
	for line in file.lines() {
        let number: i32 = line.unwrap().parse().unwrap();
        frequency += number;
    }
	assert_eq!(474 , frequency);
}