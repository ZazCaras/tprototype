<script>
	import { AiFillSmile } from 'svelte-icons-pack/ai';
	import { Icon } from 'svelte-icons-pack';

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
			title: 'Thailand’s king endorses Paetongtarn Shinawatra as new prime minister',
			content:
				' Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.  Paetongtarn Shinawatra, a scion of Thailand’s most famed and divisive political dynasty, won the endorsement of the king on Sunday to officially become the country’s new prime minister.',
			sentiment: 'Negative'
		}
	];
</script>

<svelte:head>
	<title>Positive News</title>
	<meta name="description" content="Positive News :)" />
</svelte:head>

<div>
	<h1>Positive News :)</h1>
</div>
<div class="container">
	{#each news as n, i}
		<a class="card emotion" href="#">
			<div class="overlay"></div>
			<div class="icon"><Icon src={AiFillSmile} size="43px" color="white" /></div>
			<div class="circle"></div>
			<p class="news_source">{n.source}</p>
		</a>
	{/each}
</div>

<style>
	h1 {
		color: white;
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
		--bg-color: #ffd861;
		--bg-color-light: #ffeeba;
		--text-color-hover: #4c5656;
		--box-shadow-color: rgba(255, 215, 97, 0.48);
	}

	.card {
		width: 220px;
		height: 321px;
		background: #0d3b64;
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
		width: 118px;
		position: absolute;
		height: 118px;
		border-radius: 50%;
		background: var(--bg-color);
		left: 50px;
		bottom: 75px;
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

	.icon {
		margin-bottom: 10px;
	}

	.news_source {
		font-size: 17px;
		color: #4c5656;
		z-index: 1000;
		transition: color 0.3s ease-out;
		position: absolute;
		margin-bottom: 120px;
	}

	.card:hover .news_source {
		color: var(--text-color-hover);
		position: relative;
		animation: sourceY 0.5s;
		animation-iteration-count: 1;
		animation-fill-mode: forwards;
	}

	@keyframes sourceY {
		from {
			transform: translateY(0px);
		}
		to {
			transform: translateY(100px);
		}
	}
</style>
