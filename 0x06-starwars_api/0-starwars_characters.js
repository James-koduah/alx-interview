#!/usr/bin/node

const request = require('request')

if (process.argv.length != 3){
	return;
}else{
	 
	/**
	 * function to execute reqeusts and return a promise for synchronous execution
	 */ 
	function a_request(url){
		return new Promise ((resolve, reject)=>{
			request(url, (error, response, body)=>{
				if (error) reject(error);
				resolve(JSON.parse(body))
			})
		})
	}

	async function main(){
		let movie_id = process.argv[2]
		let movie_url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id
		let movie;
		let characters;
		try{
			movie = await a_request(movie_url)
		} catch (error) {
			console.error(error)
		}
		characters = movie['characters']
		for (character of characters){
			details = await a_request(character)
			console.log(details['name'])
		}

	}
	main()

}
