<script>
	let news = [
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
		},{
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
	<title>Neutral News</title>
	<meta name="description" content="Positive News :)" />
</svelte:head>

<div>
	<h1>Neutral News :l</h1>
</div>
<div class="container">
	{#each news as n, i}
		<div class="card">
			<div><h2>{n.source}</h2></div>
			<div class="card__content">
				<p class="card__title">{n.title}</p>
				<p class="card__description">
					{n.content}
				</p>
			</div>
		</div>
	{/each}
</div>

<style>
	h1 {
		color: white;
	}
	h2 {
		color: black;
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

	/* From Uiverse.io by gharsh11032000 */
	.card {
		position: relative;
		width: 300px;
		min-height: 300px;
		max-height: 350px;
		background: linear-gradient(-45deg, #FEE3BE 0%, #916C5B 100%);
		border-radius: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;
		transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
	}

	.card:hover {
		transform: scale(1.1);
		box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
	}

	.card__content {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		width: 100%;
		height: 300px;
		padding: 20px;
		box-sizing: border-box;
		background-color: #fff;
		opacity: 0;
		transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
	}

	.card:hover .card__content {
		transform: translate(-50%, -50%) rotate(0deg);
		opacity: 1;
	}

	.card__title {
		margin: 0;
		font-size: 18px;
		color: #333;
		font-weight: 700;
		min-height: 100px;
		overflow: auto;
	}

	.card__description {
		margin: 10px 0 0;
		font-size: 12px;
		color: #777;
		line-height: 1.4;
		height: 150px;
		overflow: auto;
	}
</style>
