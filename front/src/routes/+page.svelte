<script>
	import brain from '$lib/images/BrainNoBg.png';
</script>

<svelte:head>
	<title>Sentiment News :)</title>
	<meta name="description" content="News Sentiment Analysis" />
</svelte:head>

<section>
	<img src={brain} alt="App Logo" class="bounce-in" />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}
	.bounce-in {
		animation: bounce-in 2s ease forwards;
	}
	@keyframes bounce-in {
		0% {
			opacity: 0;
			transform: scale(0.3);
		}
		50% {
			opacity: 1;
			transform: scale(1.05);
		}
		70% {
			transform: scale(0.9);
		}
		100% {
			transform: scale(1);
		}
	}
</style>
