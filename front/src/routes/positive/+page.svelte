<script>
	import { onMount } from 'svelte';
	import axios from 'axios';
	import { Icon } from 'svelte-icons-pack';
	import { FaFaceGrin } from 'svelte-icons-pack/fa';
	import { FaFaceMeh } from 'svelte-icons-pack/fa';
	import { FaFaceFrownOpen } from 'svelte-icons-pack/fa';

	let news = [];
	onMount(async () => {
		try {
			const res = await axios.get(`http://localhost:8000/news/all/positive`);
			console.log(res.data);
			news = res.data.news;
		} catch (err) {
			console.log(err);
		}
	})

	const changeSentiment = async (id, sentiment) => {
		try {
			const res = await axios.put(`http://localhost:8000/news/change/${id}`, {sentiment: sentiment});
			console.log(res.data)
			news = res.data.news;
		} catch (err) {
			console.log(err);
		}
	}

</script>

<svelte:head>
	<title>Positive News</title>
	<meta name="description" content="Positive News :)" />
</svelte:head>

<div>
	<h1>Positive News</h1>
</div>
<div class="container">
	{#each news as n, i}
		<div class="card emotion">
			<div class="overlay"></div>
			<p class="news_title">{n.title}</p>
			<p class="news_content">{n.content}</p>
			<a class="news_source" href={`/${n.source}`}>{n.website}</a>
			<div class="dropup">
				<button class="dropbtn"><Icon src={FaFaceGrin} /></button>
				<div class="dropup-content">
					<a href="#" on:click={() => changeSentiment(n.id, "positive")}><Icon src={FaFaceGrin} color="#00FA56" /></a>
					<a href="#" on:click={() => changeSentiment(n.id, "neutral")}><Icon src={FaFaceMeh} color="#F0CCA8" /></a>
					<a href="#" on:click={() => changeSentiment(n.id, "negative")}><Icon src={FaFaceFrownOpen} color="#E2253D" /></a>
				</div>
			</div>
		</div>
	{/each}
</div>

<style>
	h1 {
		color: #fedc06;
	}
	.container {
		max-width: 1200px;
		margin: 0 auto;
		display: grid;
		grid-gap: 2rem;
		margin-top: 25px;
	}

	@media (min-width: 600px) {
		.container {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (min-width: 900px) {
		.container {
			grid-template-columns: repeat(3, 1fr);
		}
	}

	.emotion {
		--bg-color: radial-gradient(
			circle,
			rgba(244, 177, 0, 1) 28%,
			rgba(254, 220, 6, 1) 75%,
			rgba(244, 177, 0, 1) 100%
		);
		--text-color-hover: #000000;
		--box-shadow-color: rgba(255, 215, 97, 0.48);
	}

	.card {
		width: 300px;
		height: 330px;
		background: black;
		border-top-right-radius: 10px;
		overflow: hidden;
		display: flex;
		flex-direction: column;
		justify-content: end;
		align-items: center;
		position: relative;
		box-shadow: 0 14px 26px rgba(0, 0, 0, 0.04);
		transition: all 0.3s ease-out;
		text-decoration: none;
	}

	.card:hover {
		transform: translateY(-5px) scale(1.005) translateZ(0);
		box-shadow:
			0 24px 36px rgba(0, 0, 0, 0.11),
			0 24px 46px var(--box-shadow-color);
	}

	.overlay {
		width: 130px;
		position: absolute;
		height: 130px;
		border-radius: 50%;
		background: var(--bg-color);
		left: 85px;
		bottom: 105px;
		z-index: 1;
		transition: transform 0.3s ease-out;
	}

	.card:hover .overlay {
		transform: scale(4) translateZ(0);
	}

	.card:active {
		transform: scale(1) translateZ(0);
		box-shadow:
			0 15px 24px rgba(0, 0, 0, 0.11),
			0 15px 24px var(--box-shadow-color);
	}

	.news_title {
		font-size: 17px;
		color: #fedc06;
		z-index: 1;
		transition: color 0.3s ease-out;
		position: absolute;
		text-align: center;
		max-height: 70px;
		overflow-y: auto;
		display: flex;
		align-items: start;
		align-content: center;
		padding: 0px 10px 10px 10px;
	}
	.card:hover .news_title {
		color: #000000;
		position: relative;
		animation: sourceY-up 1s;
		animation-iteration-count: 1;
		animation-fill-mode: forwards;
		overflow-y: auto;
	}

	.news_content {
		opacity: 0;
		position: absolute;
		z-index: 1;
	}

	.card:hover .news_content {
		color: var(--text-color-hover);
		display: inline-block;
		position: absolute;
		height: 170px;
		margin-bottom: 55px;
		overflow-y: auto;
		display: flex;
		align-content: start;
		text-align: center;
		font-size: 12px;
		padding: 10px 20px 10px 20px;
		animation: appear 2s ease forwards;
	}

	.news_source {
		font-size: 17px;
		color: #000000;
		z-index: 1;
		transition: color 0.3s ease-out;
		position: absolute;
		margin-bottom: 160px;
		max-height: 50px;
	}

	.card:hover .news_source {
		color: var(--text-color-hover);
		position: relative;
		animation: sourceY-down 0.5s;
		animation-iteration-count: 1;
		animation-fill-mode: forwards;
		max-height: 50px;
	}

	@keyframes sourceY-up {
		from {
			transform: translateY(165px);
		}
		to {
			transform: translateY(-50px);
		}
	}
	@keyframes sourceY-down {
		from {
			transform: translateY(0px);
		}
		to {
			transform: translateY(140px);
		}
	}

	@keyframes appear {
		to {
			opacity: 1;
		}
	}

	.dropup {
		position: absolute;
		bottom: 15px;
		right: 15px;
		z-index: 1;
		opacity: 0;
	}

	.card:hover .dropup {
		opacity: 0.8;
	}

	.dropbtn {
		background-color: #000000;
		color: #00fa56;
		padding: 10px;
		font-size: 16px;
		border: none;
		border-radius: 10px;
	}

	.dropup-content {
		display: none;
		position: absolute;
		background-color: black;
		bottom: 39px;
		z-index: 1;
		border-radius: 10px;
	}

	.dropup-content a {
		color: black;
		padding: 12px 10px;
		text-decoration: none;
		display: block;
		border-radius: 10px;
	}

	.dropup-content a:hover {
		background-color: rgb(95, 95, 95);
	}

	.dropup:hover .dropup-content {
		display: block;
	}
</style>
