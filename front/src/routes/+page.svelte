<script>
	import BookAnimation from '../components/BookAnimation.svelte';
	import brain from '$lib/images/BrainNoBg.png';

</script>

<svelte:head>
	<title>Sentiment News :)</title>
	<meta name="description" content="News Sentiment Analysis" />
</svelte:head>

<section>
	<img src={brain} alt="App Logo" />
	<BookAnimation/>
</section>

<style lang="postcss">
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
