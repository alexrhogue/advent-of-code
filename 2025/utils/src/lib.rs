// utils/src/lib.rs
use anyhow::Result;
use std::io::BufRead;

pub fn read_lines(path: &str) -> Result<Vec<String>> {
    let file = std::fs::File::open(path)?;
    let reader = std::io::BufReader::new(file);

    // Explicit std::result::Result so we don't collide with anyhow::Result
    Ok(reader
        .lines()
        .collect::<std::result::Result<Vec<String>, std::io::Error>>()?)
}
