<script>
	import { AiFillSmile } from 'svelte-icons-pack/ai';

	let news = [
		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN English',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		},
		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		},
		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		},
		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister Paetongtarn Paetongtarn Paetongtarn PaetongtarnPaetongtarn Paetongtarn PaetongtarnPaetongtarn',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		}, 		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN English',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		},
		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		},
		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		},
		{
			url: 'https://edition.cnn.com/2024/08/18/asia/thailand-king-paetongtarn-shinawatra-intl-hnk/index.html',
			source: 'CNN',
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister Paetongtarn Paetongtarn Paetongtarn PaetongtarnPaetongtarn Paetongtarn PaetongtarnPaetongtarn',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		}
	];
</script>

<svelte:head>
	<title>Negative News</title>
	<meta name="description" content="Negative News" />
</svelte:head>

<div>
	<h1>Negative News</h1>
</div>
<div class="container">
	{#each news as n, i}
		<a class="card emotion" href="#">
			<div class="overlay"></div>
			<p class="news_title">{n.title}</p>
			<p class="news_content">{n.content}</p>
			<p class="news_source">{n.source}</p>
		</a>
	{/each}
</div>

<style>
	h1 {
		color: #fe065d;
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
		--bg-color: radial-gradient(circle, rgba(207,0,72,1) 28%, rgba(255,59,128,1) 75%, rgba(204,0,72,1) 100%);
		--text-color-hover: #000000;
		--box-shadow-color: rgba(207,0,72, 0.48);
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
		bottom: 85px;
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
		color: #ff3b80;
		z-index: 1;
		transition: color 0.3s ease-out;
		position: absolute;
		text-align: center;
		max-height: 70px;
		overflow-y: auto
	}
	.card:hover .news_title {
		color: #000000;
		position: relative;
		animation: sourceY-up 1s;
		animation-iteration-count: 1;
		animation-fill-mode: forwards;
		max-height: 70px;
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
		margin-bottom: 135px;
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
			transform: translateY(-65px);
		}
	}
	@keyframes sourceY-down {
		from {
			transform: translateY(0px);
		}
		to {
			transform: translateY(120px);
		}
	}

	@keyframes appear {
		to {
			opacity: 1
		}	
	}
</style>
